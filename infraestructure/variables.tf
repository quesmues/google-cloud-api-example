variable "gcp_region" {
  description = "Região do GCP"
  type        = string
  default     = "southamerica-east1"
}

variable "gcp_zone" {
  description = "Zona do GCP"
  type        = string
  default     = "southamerica-east1-a"
}

variable "gcp_project_id" {
  description = "ID do projeto do GCP a ser usado"
  type        = string
  default     = "even-ally-390116"
}

variable "credentials_file" {
  description = "Caminho do arquivo onde as credenciais do GCP estão armazenadas"
  type        = string
  default     = "credentials/even-ally-390116-5a7b759021aa.json"
}

variable "github_credentials_file" {
  description = "Caminho do arquivo onde as credenciais do GitHub estão armazenadas"
  type        = string
  default     = "credentials/github-token-credentials.txt"
}

variable "service_account" {
  description = "Service account que será usada para provisionar a infraestrutura"
  type        = string
  default     = "terraform"
}

variable "github_app_instalation" {
  description = "ID da instalação do Google Cloud Build no GitHub"
  type        = string
  default     = "38715531"
}

variable "github_repo" {
  description = "Respositório do github onde o Cloud Build irá monitorar"
  type        = string
  default     = "https://github.com/quesmues/google-cloud-api-example.git"
}

variable "app_secret_key_file" {
  description = "Secret Key que será utilizada pela aplicação através da variavél secreta SECRET_KEY"
  type        = string
  default     = "credentials/secret-key.txt"
}
