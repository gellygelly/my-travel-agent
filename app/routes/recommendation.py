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
    best_months_text = next((line for line in lines if "best_months" in line), "").replace("best_months: ", "")
    best_months_text = best_months_text.strip("[]")
    best_months = [item.strip() for item in best_months_text.split(",")]
    
    spots_text =  next((line for line in lines if "recommended_spots" in line), "").replace("recommended_spots: ", "")
    spots_text = spots_text.strip("[]")
    spots = [item.strip() for item in spots_text.split(",")]
    
    return RecommendationResponse(
        best_months=best_months,
        recommended_spots=spots,
        raw_response=result
    )
