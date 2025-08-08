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