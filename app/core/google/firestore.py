from google.cloud import firestore

from app.config.settings import settings
from app.core.google.oauth2 import credentials

client = firestore.AsyncClient(project=settings.project, credentials=credentials)
