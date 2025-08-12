# 일정 계획 및 코스 추천 API

from fastapi import APIRouter
from app.agents.itinerary import generate_itinerary
from app.schemas.itinerary import ItineraryRequest, ItineraryResponse
from app.services.maps import get_distance_matrix

router = APIRouter(prefix="/itinerary", tags=["Itinerary"])

@router.post("/", response_model=ItineraryResponse)
def generate(req: ItineraryRequest):
    matrix = get_distance_matrix(req.spots)
    result = generate_itinerary(req.destination, req.days, req.spots, matrix)
    return ItineraryResponse(itinerary_plan=result, matrix=matrix)

"""
Request Body Ex 

{
  "destination": "타이베이",
  "days": 3,
  "spots": [
    "단수이", "대만 고궁박물관", "용산사", "시먼딩", "타이베이101", "스란 야시장", "중정기념당", "예스지 투어"
  ]
}
"""