from typing import Union

from pydantic import BaseModel, AnyHttpUrl, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class AwtrixHttpConfig(BaseModel):
    base_url: AnyHttpUrl
    username: str = None
    password: str = None
    verify_ssl: Union[bool, FilePath] = False


class AwtrixLightHttpClientSettings(BaseSettings):
    awtrix: AwtrixHttpConfig

    model_config = SettingsConfigDict(
        env_prefix="AWTRIX_HTTP_CLIENT_", env_file=".env", env_file_encoding="utf-8"
    )
