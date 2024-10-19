from pydantic import BaseModel

from .dns import DNSConfig
from .server import ServerConfig


class AppConfig(BaseModel):
    server: ServerConfig
    dns: DNSConfig
