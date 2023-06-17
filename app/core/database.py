from google.cloud import firestore
from google.oauth2 import service_account

from app.config.settings import settings

credentials = service_account.Credentials.from_service_account_file(settings.google_certificate_path)
client = firestore.AsyncClient(project=settings.gcp, credentials=credentials)

