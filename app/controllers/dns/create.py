import dns.asyncquery
import dns.name
from dns.update import Update

from ...models.config import AppConfig
from .base import extract_zone, initialize_update, send_update


async def create_dns_record(
    domain: str,
    ttl: int,
    record_type: str,
    response: str,
    config: AppConfig,
) -> None:
    """
    Handles the addition of a new DNS record.
    """
    zone: str = extract_zone(domain=domain, config=config)
    update: Update = initialize_update(zone=zone, config=config)
    update.add(dns.name.from_text(domain), ttl, str(record_type), str(response))
    await send_update(update=update, config=config)
