import dns.asyncquery
import dns.name
from dns.update import Update

from ...models.config import AppConfig
from .base import extract_zone, initialize_update, send_update


async def delete_dns_record(domain: str, config: AppConfig) -> None:
    """
    Handles the deletion of a DNS record.
    """
    zone: str = extract_zone(domain=domain, config=config)
    update: Update = initialize_update(zone=zone, config=config)
    update.delete(dns.name.from_text(domain))
    await send_update(update=update, config=config)
