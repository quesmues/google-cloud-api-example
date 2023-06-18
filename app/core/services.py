from typing import Dict

import aiohttp

from app.config.settings import settings


async def get_data(url: str, **data) -> Dict:
    async with aiohttp.ClientSession() as session:
        response = await session.get(url, params=data)
        if settings.debug:
            print(f"Starting request <{response.method} {response.url.path}>")
        response.raise_for_status()
        return await response.json()
