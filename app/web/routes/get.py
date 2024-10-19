from typing import Annotated, Any, Final

from fastapi import APIRouter, Query, Request

from ...controllers.dns import get_domain_records, get_zone_records
from ...models.dto import DNSRecords, ZoneRecords
from ...models.responses import DNSQueryResponse, ZoneQueryResponse

router: Final[APIRouter] = APIRouter()


@router.get(
    path="/dns/get-zone",
    response_model=ZoneQueryResponse,
    description="Retrieve all records for a specific DNS zone.",
)
async def handle_zone_query(
    request: Request,
    zone_name: Annotated[str, Query(description="Zone name to query")],
) -> Any:
    records: ZoneRecords = get_zone_records(
        zone_name=zone_name,
        config=request.app.state.config,
    )
    return ZoneQueryResponse(data=records)


@router.get(
    path="/dns/get-records",
    response_model=DNSQueryResponse,
    description="Retrieve DNS records for a specific domain.",
)
async def handle_dns_query(domain: Annotated[str, Query(description="Domain to query")]) -> Any:
    records: DNSRecords = await get_domain_records(domain)
    return DNSQueryResponse(data=records)
