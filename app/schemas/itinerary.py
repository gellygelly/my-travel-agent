from pydantic import BaseModel
from typing import List

class ItineraryRequest(BaseModel):
    destination: str
    days: int
    spots: List[str]

class DistanceMatrixEntry(BaseModel):
    origin: str
    destination: str
    distance_text: str
    duration_text: str

class ItineraryResponse(BaseModel):
    itinerary_plan: str
    matrix: List[DistanceMatrixEntry]  # 거리 정보도 응답에 포함 (원하면 생략 가능)