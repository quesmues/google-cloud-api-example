# Inicia o Google Cloud Firestore, não pode ser destruido depois de criado, 
# Boa prática seria criar o projeto todo no terraform e deletar o projeto quando for 
# destruido

# resource "google_app_engine_application" "app" {
#   project = data.google_client_config.current.project

#   location_id   = data.google_client_config.current.region
#   database_type = "CLOUD_FIRESTORE"
# }
