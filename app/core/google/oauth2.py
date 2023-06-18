from google.oauth2 import service_account

from app.config.settings import settings

try:
  credentials = service_account.Credentials.from_service_account_file(settings.gcp_certificate_path)
except TypeError:
  credentials = None
