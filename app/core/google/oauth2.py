from google.oauth2 import service_account

from app.config.settings import settings

credentials = None

if settings.gcp_certificate_path:
  credentials = service_account.Credentials.from_service_account_file(settings.gcp_certificate_path)
