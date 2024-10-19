from contextlib import suppress

import uvicorn
from fastapi import FastAPI

from .factory.app import create_app
from .factory.config import create_app_config
from .models.config import AppConfig


def main() -> None:
    config: AppConfig = create_app_config()
    app: FastAPI = create_app(config=config)
    with suppress(KeyboardInterrupt):
        return uvicorn.run(
            app=app,
            host=config.server.host,
            port=config.server.port,
        )


if __name__ == "__main__":
    main()
