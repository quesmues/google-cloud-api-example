# Criar conexão com GitHub.com

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


# IAM role para o Cloud Run

resource "google_project_iam_member" "cloud_run" {
  project = data.google_client_config.current.project
  role    = "roles/run.admin"
  member  = "serviceAccount:service-${data.google_project.project.number}@gcp-sa-cloudbuild.iam.gserviceaccount.com"
}
