# 여행지 추천 에이전트

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from app.utils.llm import get_llm

template = """
당신은 여행 컨설턴트입니다.
사용자가 여행하고자 하는 목적지는 "{destination}"입니다.

1. 이 지역을 여행하기 가장 좋은 시기(건기, 날씨, 현지 축제, 항공권 가격 등 고려)를 설명해주세요.
2. 이 목적지에서 추천하는 주요 여행 명소들을 각각 간단한 이유와 함께 설명해주세요.

1, 2번 항목에 대해 상세히 설명 후, 마지막으로, 아래와 같은 형식으로 응답을 정리해서 주세요. 아래 응답은 다른 에이전트의 입력값으로 사용되는 것입니다. 사용할 것입니다. 대괄호([])안의 항목은 반드시 단어 형태로 종결지어 주세요.

응답 형식:
best_months: [몇 월1, 몇 월2, 몇 월3, ...]
recommended_spots: [명소 이름1, 명소 이름2, 명소 이름3, ...]
...

"""

prompt = PromptTemplate.from_template(template)

def recommend_destination_info(destination: str) -> str:
    llm = get_llm()
    chain = prompt | llm
    input = {"destination": destination}
    
    result = chain.invoke(input)
    return result
