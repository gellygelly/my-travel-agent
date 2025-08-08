from fastapi import FastAPI
from app.routes import recommendation, itinerary, travel_plan

app = FastAPI(title="My Travel Agent",
            docs_url="/docs")

app.include_router(recommendation.router)
app.include_router(itinerary.router)
app.include_router(travel_plan.router)