from typing import Any

from pydantic import BaseModel

from .dto import DNSRecords, ZoneRecords


class BaseResponse(BaseModel):
    ok: bool = True
    data: Any
    message: str


class ZoneQueryResponse(BaseResponse):
    data: ZoneRecords
    message: str = "Zone records retrieved successfully."


class DNSQueryResponse(BaseResponse):
    data: DNSRecords
    message: str = "DNS records retrieved successfully."


class CreateDNSRecordResponse(BaseResponse):
    data: bool = True
    message: str = "DNS record created successfully."


class DeleteDNSRecordResponse(BaseResponse):
    data: bool = True
    message: str = "DNS record deleted successfully."


class UpdateDNSRecordResponse(BaseResponse):
    data: bool = True
    message: str = "DNS record updated successfully."
