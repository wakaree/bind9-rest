from .create import create_dns_record
from .delete import delete_dns_record
from .get import get_domain_records, get_zone_records
from .update import update_dns_record

__all__ = [
    "create_dns_record",
    "delete_dns_record",
    "get_domain_records",
    "get_zone_records",
    "update_dns_record",
]
