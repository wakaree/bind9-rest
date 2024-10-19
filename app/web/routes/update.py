from typing import Any, Final

from fastapi import APIRouter, Body, Request

from ...controllers.dns import update_dns_record
from ...models.dto import DNSRecord
from ...models.responses import UpdateDNSRecordResponse

router: Final[APIRouter] = APIRouter()


@router.put(
    path="/dns/update-record",
    response_model=UpdateDNSRecordResponse,
    description="Update existing DNS records.",
)
async def update_record(
    request: Request,
    dns_record: DNSRecord = Body(description="Details for the DNS record."),
) -> Any:
    await update_dns_record(
        domain=dns_record.domain,
        ttl=dns_record.ttl,
        record_type=dns_record.record_type,
        response=dns_record.response,
        config=request.app.state.config,
    )
    return UpdateDNSRecordResponse()
