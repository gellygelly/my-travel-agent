# 여행 체크리스트 생성 에이전트

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from app.utils.llm import get_llm
from app.schemas.checklist import ChecklistRequest

template = """
당신은 여행 준비 전문가입니다.

다음 정보를 바탕으로 여행 체크리스트를 구성해주세요:

- 여행 국가: {country}
- 여행 유형: {trip_type}
- 여행 기간: {days}일
- 계절: {season}
- 여행 목적: {purpose}

{travel_spots_info}

체크리스트 항목:
1. 해당 국가의 전압/플러그 정보와 돼지코 필요 여부
2. 현지 교통카드/패스 정보
3. 인천공항 스마트패스, ETA, 전자입국증 등 필요한 입출국 관련 준비사항
4. 일반적인 공통 준비물 (여권, 충전기, 약, 옷 등)
5. 해당 국가나 기후에 따라 꼭 필요한 특별 준비물
6. 방문 장소별로 필요한 추가 준비물 (예: 등산화, 수영복, 방수팩 등)

결과를 아래 형식에 맞춰 작성해주세요:

[요약 설명]
...

[전압 및 플러그 정보]
...

[입출국 준비 서류]
- ...

[교통 카드/패스]
- ...

[공통 준비물]
- ...

[해당 국가 전용 준비물]
- ...

[일정 기반 준비물]
- ...
"""

def generate_checklist(request: ChecklistRequest):
    llm = get_llm()
    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm

    if request.travel_spots:
        travel_spots_info = f"사용자는 다음 장소들을 방문할 예정입니다:\n" + \
                            "\n".join(f"- {s}" for s in request.travel_spots)
    else:
        travel_spots_info = ""

    result = chain.invoke({
        "country": request.country,
        "trip_type": request.trip_type, # 패키지, 자유여행 등
        "days": request.days,
        "season": request.season,
        "purpose": request.purpose,
        "travel_spots_info": travel_spots_info
    })

    return result
