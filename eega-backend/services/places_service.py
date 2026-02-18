from pydantic import BaseModel


class Place(BaseModel):
    type: str
    name: str
    eta_minutes: int
    distance_km: float


class NearbyPlacesResponse(BaseModel):
    items: list[Place]


def get_nearby_places(latitude: float, longitude: float) -> NearbyPlacesResponse:
    """
    Placeholder implementation.

    Swap this out with real calls to Google Places, OpenStreetMap, or another service.
    """
    _ = (latitude, longitude)  # unused for now

    demo = [
        Place(type="Hospital", name="Demo General Hospital", eta_minutes=6, distance_km=2.1),
        Place(type="Police", name="Demo City Police Station", eta_minutes=9, distance_km=3.4),
        Place(type="Fire", name="Demo Fire & Rescue", eta_minutes=11, distance_km=4.0),
    ]
    return NearbyPlacesResponse(items=demo)

