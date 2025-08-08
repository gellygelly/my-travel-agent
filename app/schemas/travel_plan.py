from typing import List
from pydantic import BaseModel
from app.schemas.itinerary import DistanceMatrixEntry

class TravelPlanRequest(BaseModel):
    destination: str  # 목적지 / 예: 대만
    days: int         # 여행일수 / 예: 3
    season: str       # 여름 / 겨울 등
    purpose: str      # 휴양, 맛집투어 등


class TravelPlanResponse(BaseModel):
    best_season: str
    recommended_spots: List[str]
    itinerary: str
    distance_matrix: List[DistanceMatrixEntry]
    checklist: dict  # ChecklistResponse를 그대로 사용해도 됨 (간단화를 위해 dict 처리)