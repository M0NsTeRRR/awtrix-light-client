from pydantic import ValidationError
import pytest

from awtrix_light_client.http_settings import AwtrixLightHttpClientSettings


async def test_no_settings():
    with pytest.raises(ValidationError):
        AwtrixLightHttpClientSettings()


async def test_wrong_url(monkeypatch):
    monkeypatch.setenv("AWTRIX_HTTP_CLIENT_AWTRIX", '{"base_url": "test"}')

    with pytest.raises(ValidationError):
        AwtrixLightHttpClientSettings()


async def test_works_no_auth(monkeypatch):
    monkeypatch.setenv("AWTRIX_HTTP_CLIENT_AWTRIX", '{"base_url": "http://test.fr"}')

    AwtrixLightHttpClientSettings()


async def test_works_auth(monkeypatch):
    monkeypatch.setenv(
        "AWTRIX_HTTP_CLIENT_AWTRIX",
        '{"base_url": "http://test.fr", "auth": "username", "password": "password"}',
    )

    AwtrixLightHttpClientSettings()
