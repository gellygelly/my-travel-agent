# 여행 준비 체크리스트 API

from fastapi import APIRouter
from app.schemas.checklist import ChecklistRequest, ChecklistResponse
from app.agents.checklist import generate_checklist

router = APIRouter(prefix="/checklist", tags=["Checklist"])

@router.post("/", response_model=ChecklistResponse)
def create_checklist(req: ChecklistRequest):
    """
    사용자의 국가, 계절, 목적, 여행 장소 등을 기반으로 맞춤형 준비물 리스트 제공
    """
    result = generate_checklist(req)

    return ChecklistResponse(
        summary=result["summary"],
        power_info=result["power_info"],
        travel_docs=result["travel_docs"],
        transport_tips=result["transport_tips"],
        essential_items=result["essential_items"],
        country_specific_items=result["country_specific_items"],
        raw_response=result["raw_response"]
    )