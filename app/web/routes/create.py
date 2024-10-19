from typing import Any, Final

from fastapi import APIRouter, Body, Request

from ...controllers.dns import create_dns_record
from ...models.dto import DNSRecord
from ...models.responses import CreateDNSRecordResponse

router: Final[APIRouter] = APIRouter()


@router.post(
    path="/dns/add-record",
    response_model=CreateDNSRecordResponse,
    description="Create or update DNS records.",
)
async def create_record(
    request: Request,
    dns_record: DNSRecord = Body(description="Details for the DNS record."),
) -> Any:
    await create_dns_record(
        domain=dns_record.domain,
        ttl=dns_record.ttl,
        record_type=dns_record.record_type,
        response=dns_record.response,
        config=request.app.state.config,
    )
    return CreateDNSRecordResponse()
