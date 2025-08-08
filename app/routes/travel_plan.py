# 여행 계획 종합 추천 API

from fastapi import APIRouter
from app.schemas.travel_plan import TravelPlanRequest, TravelPlanResponse
from app.agents.recommendation import recommend_destination_info
from app.agents.itinerary import generate_itinerary
from app.services.maps import get_distance_matrix
from app.agents.checklist import generate_checklist
from app.schemas.checklist import ChecklistRequest

router = APIRouter(prefix="/travel-plan", tags=["Travel Plan"])

@router.post("/", response_model=TravelPlanResponse)
def create_travel_plan(req: TravelPlanRequest):
    # 1. 여행지 추천
    rec_result = recommend_destination_info(req.destination)
    spots = rec_result.recommended_spots
    best_months = rec_result.best_months

    # 2. 여행지별 거리 계산
    matrix = get_distance_matrix(spots)

    # 3. 일정 생성
    itinerary_result = generate_itinerary(req.destination, req.days, spots, matrix)

    # 4. 체크리스트 생성 (여행 코스 포함)
    checklist_req = ChecklistRequest(
        country=req.destination,
        trip_type="해외여행",  # 기본값
        days=req.days,
        season=req.season,
        purpose=req.purpose,
        travel_spots=spots
    )
    
    checklist = generate_checklist(checklist_req)

    return TravelPlanResponse(
        best_season=best_season,
        recommended_spots=spots,
        itinerary=itinerary_result,
        distance_matrix=matrix,
        checklist=checklist
    )
