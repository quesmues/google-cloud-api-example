# Criar conexão com GitHub.com

resource "google_secret_manager_secret" "github-token-secret" {
  provider  = google-beta
  secret_id = "github-token-secret"

  replication {
    automatic = true
  }
}

data "google_iam_policy" "p4sa-secretAccessor" {
  provider = google-beta
  binding {
    role    = "roles/secretmanager.secretAccessor"
    members = ["serviceAccount:service-${data.google_project.project.number}@gcp-sa-cloudbuild.iam.gserviceaccount.com"]
  }
}

resource "google_secret_manager_secret_version" "github-token-secret-version" {
  provider    = google-beta
  secret      = google_secret_manager_secret.github-token-secret.id
  secret_data = file(var.github_credentials_file)
}

resource "google_secret_manager_secret_iam_policy" "policy" {
  provider    = google-beta
  secret_id   = google_secret_manager_secret.github-token-secret.secret_id
  policy_data = data.google_iam_policy.p4sa-secretAccessor.policy_data
}


resource "google_cloudbuildv2_connection" "my-connection" {
  provider = google-beta
  location = data.google_client_config.current.region
  name     = "my-connection"

  github_config {
    app_installation_id = var.github_app_instalation
    authorizer_credential {
      oauth_token_secret_version = google_secret_manager_secret_version.github-token-secret-version.id
    }
  }

  depends_on = [
    google_secret_manager_secret_iam_policy.policy,
  ]
}

# IAM role para o Cloud Builder

resource "google_project_iam_member" "build_editor" {
  project = data.google_client_config.current.project
  role    = "roles/cloudbuild.builds.editor"
  member  = data.google_service_account.current.member
}

# Trigger do Cloud Builder

resource "google_cloudbuildv2_repository" "my-repository" {
  provider          = google-beta
  name              = "my-repo"
  parent_connection = google_cloudbuildv2_connection.my-connection.id
  remote_uri        = var.github_repo
}

resource "google_cloudbuild_trigger" "repo-trigger" {
  provider = google-beta
  location = data.google_client_config.current.region

  repository_event_config {
    repository = google_cloudbuildv2_repository.my-repository.id
    push {
      tag = ".*"
    }
  }

  filename = "cloudbuild.yaml"
}
