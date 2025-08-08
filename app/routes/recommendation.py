# 여행지 추천 API

from fastapi import APIRouter
from app.agents.recommendation import recommend_destination_info
from app.schemas.recommendation import RecommendationRequest, RecommendationResponse

router = APIRouter(prefix="/recommendation", tags=["Recommendation"])

@router.post("/", response_model=RecommendationResponse)
def recommend(req: RecommendationRequest):
    result = recommend_destination_info(req.destination)

    # 간단한 후처리 (LLM 응답 포맷에 따라 조정 가능)
    lines = [line.strip() for line in result.split("\n") if line.strip()]
    best_season = next((line for line in lines if "시기" in line or "좋은 시기" in line), "")
    spots = [line for line in lines if any(keyword in line.lower() for keyword in ["추천", "명소", "관광지", "spot"])]
    spots = spots[:5] if len(spots) >= 5 else spots

    return RecommendationResponse(
        best_season=best_season,
        recommended_spots=spots,
        raw_response=result
    )
