from typing import Annotated, Final

from fastapi import HTTPException, Request, Security, status
from fastapi.security import APIKeyHeader

from ..models.config import AppConfig

api_key_header: Final[APIKeyHeader] = APIKeyHeader(name="Authorization")


async def verify_api_token(
    request: Request,
    api_token: Annotated[str, Security(api_key_header)],
) -> None:
    config: AppConfig = request.app.state.config
    if api_token != config.server.api_token.get_secret_value():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API-Token header invalid",
        )
