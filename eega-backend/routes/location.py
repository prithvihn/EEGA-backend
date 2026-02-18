from fastapi import APIRouter
from pydantic import BaseModel

from services.places_service import NearbyPlacesResponse, get_nearby_places


class LocationBody(BaseModel):
    latitude: float
    longitude: float


router = APIRouter()


@router.post("/nearby", response_model=NearbyPlacesResponse)
async def nearby_places(body: LocationBody):
    return get_nearby_places(latitude=body.latitude, longitude=body.longitude)

