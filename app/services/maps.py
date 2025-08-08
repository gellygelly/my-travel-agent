# Google Maps API를 이용한 이동 거리/시간 계산

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
        url = "https://routes.googleapis.com/directions/v2:computeRoutes"
        params = {
            "origin": origin,
            "destination": destination,
            "travelMode": "transit",  # 대중교통 기준
            "key": GOOGLE_MAPS_API_KEY
        }
        res = requests.post(url, params=params).json()

        print('구글 Maps API 응답 확인용: {res}')
        element = res["rows"][0]["elements"][0]

        entries.append(DistanceMatrixEntry(
            origin=origin,
            destination=destination,
            distance_text=element["distance"]["text"],
            duration_text=element["duration"]["text"]
        ))

    return entries

