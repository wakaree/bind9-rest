from ..models.config.env import AppConfig, DNSConfig, ServerConfig


def create_app_config() -> AppConfig:
    return AppConfig(server=ServerConfig(), dns=DNSConfig())
