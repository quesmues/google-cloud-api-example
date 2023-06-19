# Inicia a fila do Cloud Tasks, necessita de um google_app_engine_application

resource "google_cloud_tasks_queue" "default" {
  location = var.gcp_region
  name     = "${var.gcp_project_id}-queue"

  retry_config {
    max_attempts = 5
  }
}
