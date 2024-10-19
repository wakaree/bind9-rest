from typing import Any, Final

from fastapi import APIRouter, Body, Request

from ...controllers.dns import delete_dns_record
from ...models.dto import DNSDomain
from ...models.responses import DeleteDNSRecordResponse

router: Final[APIRouter] = APIRouter()


@router.delete(
    path="/dns/delete-record",
    response_model=DeleteDNSRecordResponse,
    description="Delete existing DNS records.",
)
async def delete_record(
    request: Request,
    dns_domain: DNSDomain = Body(description="Details for the DNS record."),
) -> Any:
    await delete_dns_record(
        domain=dns_domain.domain,
        config=request.app.state.config,
    )
    return DeleteDNSRecordResponse()
