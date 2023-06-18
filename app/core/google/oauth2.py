from google.oauth2 import service_account

from app.config.settings import settings

try:
  credentials = service_account.Credentials.from_service_account_file(settings.gcp_certificate_path)
except Exception:
  import google.auth
  credentials, project_id = google.auth.default(scopes=settings.scopes)
