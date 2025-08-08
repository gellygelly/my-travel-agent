# 여행지 추천

from pydantic import BaseModel
from typing import List

class RecommendationRequest(BaseModel):
    destination: str  # 예: 타이페이

class RecommendationResponse(BaseModel):
    best_months: List[str]
    recommended_spots: List[str]
    raw_response: str
