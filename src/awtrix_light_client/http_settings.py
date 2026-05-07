from pydantic import AnyHttpUrl, BaseModel, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class AwtrixHttpConfig(BaseModel):
    """Base model representing API configuration

    :param base_url: Base URL of API
    :param username: username when using HTTP basic auth
    :param password: password when using HTTP basic auth
    :param verify: SSL certificates (a.k.a CA bundle) used to verify the identity of requested hosts. Either True (default CA bundle), a path to an SSL certificate file, or False (which will disable verification).
    """

    base_url: AnyHttpUrl
    username: str | None = None
    password: str | None = None
    verify_ssl: bool | FilePath = False


class AwtrixLightHttpClientSettings(BaseSettings):
    awtrix: AwtrixHttpConfig

    model_config = SettingsConfigDict(
        env_prefix="AWTRIX_HTTP_CLIENT_", env_file=".env", env_file_encoding="utf-8"
    )
