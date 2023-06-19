# GitHub acess key

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


# Aplication Secret key (SECRET_KEY)

resource "google_secret_manager_secret" "app-secret-key" {
  provider  = google-beta
  secret_id = "app-secret-key"

  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret_version" "app-secret-key-version" {
  provider    = google-beta
  secret      = google_secret_manager_secret.app-secret-key.id
  secret_data = file(var.app_secret_key_file)
}
