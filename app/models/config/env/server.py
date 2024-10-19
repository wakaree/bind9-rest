from pydantic import SecretStr

from .base import EnvSettings


class ServerConfig(EnvSettings, env_prefix="SERVER_"):
    port: int
    host: str
    api_token: SecretStr
