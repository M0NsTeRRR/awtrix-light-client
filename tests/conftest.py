from contextlib import asynccontextmanager
from typing import AsyncIterator
import pytest

from awtrix_light_client.http_client import (
    AwtrixLightHttpClient,
    get_awtrix_http_client,
)


@pytest.fixture
@asynccontextmanager
async def awtrix_http_client(monkeypatch) -> AsyncIterator[AwtrixLightHttpClient]:
    monkeypatch.setenv("AWTRIX_HTTP_CLIENT_AWTRIX", '{"base_url": "http://test/"}')
    async with get_awtrix_http_client() as client:
        yield client
