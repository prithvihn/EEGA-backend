from fastapi import APIRouter
from pydantic import BaseModel

from services.llm_service import generate_guidance


class EmergencyRequest(BaseModel):
    description: str
    latitude: float | None = None
    longitude: float | None = None


router = APIRouter()


@router.post("/")
async def handle_emergency(payload: EmergencyRequest):
    guidance = generate_guidance(
        description=payload.description,
        latitude=payload.latitude,
        longitude=payload.longitude,
    )
    return {"guidance": guidance}

