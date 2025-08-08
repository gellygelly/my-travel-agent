# 일정 계획 및 코스 추천 에이전트

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from app.utils.llm import get_llm
from app.schemas.itinerary import DistanceMatrixEntry

template = """
당신은 여행 일정 설계 전문가입니다.

여행지는 {destination}, 일정은 총 {days}일입니다.
사용자가 방문하고자 하는 장소는 아래와 같습니다:

{spot_list}

아래는 각 장소 간 이동 거리 및 시간입니다:

{distance_info}

이 정보를 참고하여, 장소 간 이동을 최소화하고 각 일자별로 현실적인 일정을 만들어주세요.
1일차부터 N일차까지 장소 방문 순서와 간단한 설명을 포함해 일정을 구성해주세요.
"""

prompt = PromptTemplate.from_template(template)

def generate_itinerary(destination: str, days: int, spots: list[str], distances: list[DistanceMatrixEntry]) -> str:
    llm = get_llm()
    chain = LLMChain(llm=llm, prompt=prompt)

    spot_list = "\n".join(f"- {s}" for s in spots)
    distance_info = "\n".join(
        f"- {d.origin} → {d.destination}: {d.distance_text} / {d.duration_text}"
        for d in distances
    )

    result = chain.run({
        "destination": destination,
        "days": days,
        "spot_list": spot_list,
        "distance_info": distance_info
    })
    return result

