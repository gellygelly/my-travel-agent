from pydantic import BaseModel
from typing import List, Optional

class ChecklistRequest(BaseModel):
    country: str
    trip_type: str
    days: int
    season: str
    purpose: str
    travel_spots: Optional[List[str]] = None  # 일정 기반 장소 정보 추가(여행 코스)

class ChecklistResponse(BaseModel):
    summary: str
    essential_items: List[str]
    country_specific_items: List[str]
    travel_docs: List[str]
    transport_tips: List[str]
    power_info: str
    raw_response: str
