from fastapi import Security
from fastapi.security import APIKeyHeader

from src.configs.application import get_settings
from src.exceptions.authentication_failed import AuthenticationFailed


async def api_key(
    api_key_header: str = Security(APIKeyHeader(name="x-api-key", auto_error=False)),
):
    if get_settings().API_KEY is None:
        raise AuthenticationFailed("Master key disabled")
    if api_key_header != get_settings().API_KEY:
        raise AuthenticationFailed("Invalid key")
