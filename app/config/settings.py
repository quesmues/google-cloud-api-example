import logging
import os
import pathlib

from dotenv import load_dotenv
from pydantic import BaseSettings

filepath = pathlib.Path(__file__).resolve().parent.parent

load_dotenv(str(filepath) + "/.env")

class Settings(BaseSettings):
    debug: bool = os.getenv("DEBUG")
    app_name: str = "Google Cloud API Example"
    version: str = "0.0.3"
    prefix_v1: str = "/api/v1"
    
    # Certificado apenas em ambiente local
    gcp_certificate_path: str = os.getenv("GCP_CERTIFICATE_PATH")
    
    # Auth Scopes
    scopes: list = [os.getenv("GCP_AUTH_SCOPE")]
    
    project: str = os.getenv("GCP_PROJECT_ID")
    region: str = os.getenv("GCP_REGION")
    queue_name: str = f"{project}-queue"
    queue: str = f"projects/{project}/locations/{region}/queues/{queue_name}"
    service_name: str = os.getenv("GCP_RUN_SERVICE_NAME")
    service: str = f"projects/{project}/locations/{region}/services/{service_name}"
    

    
    # Integração API FIPE https://deividfortuna.github.io/fipe/
    fipe_url: str = os.getenv("FIPE_BASE_URL")
    

settings = Settings()

if settings.debug:
    logging.basicConfig(level=logging.DEBUG)
