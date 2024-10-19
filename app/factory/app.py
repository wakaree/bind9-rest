import logging
from logging import basicConfig
from typing import Any

from fastapi import Depends, FastAPI, HTTPException, Request, status

from ..models.config import AppConfig
from ..web.depends import verify_api_token
from ..web.routes import create, delete, get, update


# noinspection PyUnusedLocal
async def provide_error_details(request: Request, error: Exception) -> Any:
    logging.exception(error)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=str(error),
    )


def create_app(config: AppConfig) -> FastAPI:
    basicConfig(level=logging.INFO)
    app: FastAPI = FastAPI(
        prefix="/api",
        dependencies=[Depends(verify_api_token)],
    )
    app.add_exception_handler(ValueError, provide_error_details)
    app.state.config = config
    app.include_router(create.router)
    app.include_router(delete.router)
    app.include_router(get.router)
    app.include_router(update.router)
    return app
