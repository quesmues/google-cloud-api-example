output "region" {
  value = data.google_client_config.current.region
}

output "project" {
  value = data.google_client_config.current.project
}

output "queue" {
  value = google_cloud_tasks_queue.default
}
