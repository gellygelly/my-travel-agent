# 여행지 추천 에이전트

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from app.utils.llm import get_llm

template = """
당신은 여행 컨설턴트입니다.
사용자가 여행하고자 하는 목적지는 "{destination}"입니다.

1. 이 지역을 여행하기 가장 좋은 시기(건기, 날씨, 현지 축제, 항공권 가격 등 고려)를 설명해주세요.
2. 이 목적지에서 추천하는 주요 여행 명소들을 각각 간단한 이유와 함께 설명해주세요.
"""

prompt = PromptTemplate.from_template(template)

def recommend_destination_info(destination: str) -> str:
    llm = get_llm()
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(destination=destination)
    return result
