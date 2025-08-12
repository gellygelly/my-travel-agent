# 🧭 My Travel Agent 🧭

나만의 여행 도우미 에이전트 😎
귀찮고 번거로운 여행 정보 서치 및 준비 과정을 돕기 위한 에이전트!

---

## 💡 Overview

- 여행지 관련 정보 추천 Agent
    - 해당 나라에 방문하기 좋은 시기, 주요 관광 스팟 추천
- 여행 계획 수립 Agent
    - 여행지, 일정, 방문하는 관광 스팟을 기반으로 각 장소 간 거리를 고려하여 일자별 코스 추천
- 여행 체크리스트 생성 Agent
    - 사용자가 방문하려는 국가, 계절, 목적, 여행 장소, 일정을 바탕으로 여행을 위한 체크리스트 생성
- 나만의 여행 플래너 Agent
    - 여행지 관련 정보 추천부터 이에 따른 일자별 여행 코스, 여행 체크리스트 제안, 그리고 여행 관련 상품 검색 및 제안부터 일정 등록까지 목표로 하는 여행 플래너 에이전트

---

## ⚙️ 기술 스택(정리 중)

| 영역 | 기술 |
|------|------|
| 언어 | Python 3.10 |
| Backend | FastAPI |
| Frontend | Stremalit(예정) |
| LLM | OpenAI gpt-oss:20b / Ollama |
| Prompting | LangChain PromptTemplate, Chain |
| 외부 API | Google Maps API (예정), ... |
| 벡터 검색 (RAG) | MongoDB + VectorDB (예정) |
| 데이터 저장 | MongoDB (예정) |
| 배포 (예정) | Docker |

---

## 🔧 Development Checklist

### ✅ `/recommendation` - 여행지 정보 추천 API 
### 🔲 `/itinerary` - 일정 계획 및 코스 추천 API 
### ✅ `/checklist` - 여행 체크리스트 생성 API 
### 🔲 `/travel-plan` - 종합적인 여행 플랜 제안 API 
### 🔲 Streamlit Web UI 지원
### 🔲 (고도화 단계) Google/Naver 등 Calendar 연동 & 알람
### 🔲 (고도화 단계) 항공권, 숙소, 투어 등의 상품 검색 및 제안 기능

