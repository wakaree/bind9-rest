import dns.query
import dns.zone
from dns.asyncresolver import Resolver
from dns.rdatatype import SOA
from dns.resolver import NXDOMAIN, NoAnswer

from ...enums.record_type import RecordType
from ...models.config import AppConfig
from ...models.dto import DNSRecords, ZoneRecord, ZoneRecords
from .base import validate_zone


def get_zone_records(zone_name: str, config: AppConfig) -> ZoneRecords:
    """
    Fetches all records for a specific zone.
    """
    zone_name = validate_zone(zone=zone_name, config=config)

    try:
        zone_transfer = dns.query.xfr(
            where=config.dns.server,
            zone=zone_name,
            keyring=config.dns.tsig_keyring,
        )
        zone = dns.zone.from_xfr(zone_transfer)
    except dns.exception.DNSException as error:
        raise ValueError(str(error))

    records: dict[str, list[ZoneRecord]] = {}
    for name, ttl, rdata in zone.iterate_rdatas():
        if rdata.rdtype != SOA:
            record = ZoneRecord(
                name=str(name),
                ttl=ttl,
                record_type=rdata.rdtype,
                answer=str(rdata),
            )
            records.setdefault(str(name), []).append(record)

    return ZoneRecords(zone_name=zone_name, records=records)


async def get_domain_records(domain: str) -> DNSRecords:
    """
    Fetches DNS records for a specific domain.
    """
    records: dict[str, list[str]] = {}
    resolver: Resolver = Resolver()

    for record_type in RecordType:
        try:
            answers = await resolver.resolve(domain, record_type)
            if answers.rrset is None:
                continue
            records[record_type] = [str(rdata) for rdata in answers.rrset]
        except (NoAnswer, NXDOMAIN):
            continue

    return DNSRecords(domain=domain, records=records)
