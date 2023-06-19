provider "google" {
  credentials = file(var.credentials_file)

  project = var.gcp_project_id
  region  = var.gcp_region
  zone    = var.gcp_zone
}

provider "google-beta" {
  credentials = file(var.credentials_file)

  project = var.gcp_project_id
  region  = var.gcp_region
  zone    = var.gcp_zone
}
