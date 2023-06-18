from google.cloud.run_v2.services.services.client import ServicesClient

from app.config.settings import settings
from app.core.google.oauth2 import credentials

_client = ServicesClient(credentials=credentials)

_service = _client.get_service(name=settings.service)

uri = _service.uri