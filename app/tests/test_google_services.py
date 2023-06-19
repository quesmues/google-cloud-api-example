from unittest.mock import MagicMock, patch

import pytest

from app.core.google.tasks import create_http_task


@patch("app.core.google.tasks.tasks_client")
@pytest.mark.asyncio
async def test_create_http_task(tasks_client_mock):
    tasks_client_mock.queue_path = MagicMock(return_value="string")
    _ = await create_http_task("/uri", {"data": "teste"})
    assert tasks_client_mock.queue_path.call_count >= 1
    assert tasks_client_mock.create_task.call_count >= 1
