import dns.asyncquery
import dns.name
import dns.tsigkeyring
import dns.update
from dns.message import Message

from ...models.config import AppConfig


def validate_zone(zone: str, config: AppConfig) -> str:
    """
    Validates if the given zone is in the list of valid zones.
    """
    if not zone.endswith("."):
        zone += "."
    if zone not in config.dns.valid_zones:
        raise ValueError("Zone not permitted")
    return zone


def extract_zone(domain: str, config: AppConfig) -> str:
    """
    Extracts the zone from a fully qualified domain name (FQDN).
    """
    if not domain.endswith("."):
        domain += "."
    for zone in config.dns.valid_zones:
        if domain.endswith(zone):
            return zone
    raise ValueError("Zone not permitted")


def initialize_update(zone: str, config: AppConfig) -> dns.update.Update:
    """
    Initializes the DNS update object with TSIG keyring for the given zone.
    """
    return dns.update.Update(zone=zone, keyring=config.dns.tsig_keyring)


async def send_update(update: dns.update.Update, config: AppConfig) -> None:
    """
    Sends a DNS update to the specified server.
    """
    response: Message = await dns.asyncquery.tcp(q=update, where=config.dns.server)
    if response.rcode() != 0:
        raise ValueError(f"DNS update failed: {response.rcode()}")
