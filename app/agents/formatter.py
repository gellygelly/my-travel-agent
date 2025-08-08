# 사용자 여행 일정 설명 도우미 에이전트

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from app.utils.llm import get_llm
from app.schemas.itinerary import DistanceMatrixEntry

formatter_template = """
당신은 여행 일정을 사용자에게 설명하는 도우미입니다.

여행 목적지: {destination}
여행 기간: {days}일
방문할 장소: 
{spots}

각 장소 간의 거리/시간 정보:
{distances}

위 일정을 보기 쉽게 요약해주세요. 날짜별로 어떤 장소를 방문하는지 말해주고, 
표 형식으로 정리한 후 마지막에 간단한 요약 설명도 추가해주세요.
"""

def format_itinerary_output(destination: str, days: int, spots: list[str], distances: list[DistanceMatrixEntry]):
    llm = get_llm()
    prompt = PromptTemplate.from_template(formatter_template)
    
    distance_info = "\n".join(
        f"- {d.origin} → {d.destination}: {d.distance_text}, {d.duration_text}"
        for d in distances
    )
    joined_spots = "\n".join(f"- {s}" for s in spots)

    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({
        "destination": destination,
        "days": days,
        "spots": joined_spots,
        "distances": distance_info
    })
    return result