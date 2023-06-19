import json
from typing import Dict

from google.cloud import tasks_v2

from app.config.settings import settings
from app.core.google.oauth2 import credentials
from app.core.google.service import uri

tasks_client = tasks_v2.CloudTasksClient(credentials=credentials)

async def create_http_task(relative_uri: str,  payload: Dict):
    """ 
    Cria e envia a task para ser executada, através do Cloud Run
    
    
    app_url: url da própria app no Cloud Run que a task irá executar    
    """
    task = tasks_v2.Task(
        http_request=tasks_v2.HttpRequest(
            http_method=tasks_v2.HttpMethod.POST,
            url = f"{uri}{relative_uri}",
            headers={"Content-type": "application/octet-stream"},
            body=json.dumps(payload).encode(),
        )
    )

    response = tasks_client.create_task(
        tasks_v2.CreateTaskRequest(
            parent=tasks_client.queue_path(settings.project, settings.region, queue=settings.queue_name),
            task=task,
        )
    )
    return response
