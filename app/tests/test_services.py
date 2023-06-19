from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.core.services import get_data


@patch("app.core.services.aiohttp.ClientSession")
@pytest.mark.asyncio
async def test_get_data(session_mock):
    session = AsyncMock()
    get = AsyncMock()
    json = AsyncMock(return_value={"teste": "data"})
    get.json = json
    get.raise_for_status = MagicMock()
    session.get.return_value = get

    session_mock.return_value.__aenter__.return_value = session
    results = await get_data("teste", data="data")

    assert json.call_count >= 1
    assert results == {"teste": "data"}
