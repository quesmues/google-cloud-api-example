import logging
import os
import pathlib

from dotenv import load_dotenv
from pydantic import BaseSettings

filepath = pathlib.Path(__file__).resolve().parent.parent

load_dotenv(str(filepath) + "/.env")


class Settings(BaseSettings):
    debug: bool = os.getenv("DEBUG")
    app_name: str = "Hello World Example"
    version: str = "0.0.1"
    prefix_v1: str = "/api/v1"

settings = Settings()

if settings.debug:
    logging.basicConfig(level=logging.DEBUG)
