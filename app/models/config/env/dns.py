from typing import Any

import dns.name
import dns.tsig
import dns.tsigkeyring
from pydantic import Field, SecretStr

from ....utils.custom_types import StringList
from .base import EnvSettings


class DNSConfig(EnvSettings, env_prefix="DNS_"):
    server: str
    valid_zones: StringList
    tsig_username: str
    tsig_password: SecretStr
    tsig_keyring: dict[dns.name.Name, dns.tsig.Key] = Field(default_factory=dict)

    def model_post_init(self, __context: Any) -> None:
        tsig: dict[str, str] = {self.tsig_username: self.tsig_password.get_secret_value()}
        self.valid_zones = [
            f"{zone}." if not zone.endswith(".") else zone
            for zone in self.valid_zones
        ]
        self.tsig_keyring = dns.tsigkeyring.from_text(tsig)
