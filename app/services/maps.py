# 이동 거리/시간 계산

import os
import requests
from app.schemas.itinerary import DistanceMatrixEntry

GOOGLE_MAPS_API_KEY = os.getenv("MAPS_API_KEY")

def get_distance_matrix(locations: list[str]) -> list[DistanceMatrixEntry]:
    origin_dest_pairs = [
        (locations[i], locations[i + 1])
        for i in range(len(locations) - 1)
    ]

    entries = []
    for origin, destination in origin_dest_pairs:
        url = "https://maps.googleapis.com/maps/api/distancematrix/json"
        params = {
            "origins": origin,
            "destinations": destination,
            "mode": "transit",  # 대중교통 기준
            "key": GOOGLE_MAPS_API_KEY
        }
        res = requests.get(url, params=params).json()
        element = res["rows"][0]["elements"][0]

        entries.append(DistanceMatrixEntry(
            origin=origin,
            destination=destination,
            distance_text=element["distance"]["text"],
            duration_text=element["duration"]["text"]
        ))

    return entries

