from pydantic import BaseModel

from ..enums.record_type import RecordType


class DNSDomain(BaseModel):
    domain: str


class DNSRecord(DNSDomain):
    ttl: int
    record_type: RecordType
    response: str


class ZoneRecord(BaseModel):
    name: str
    ttl: int
    record_type: str
    answer: str


class DNSRecords(BaseModel):
    domain: str
    records: dict[str, list[str]]


class ZoneRecords(BaseModel):
    zone_name: str
    records: dict[str, list[ZoneRecord]]
