from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import emergency, location

app = FastAPI(title="EEGA Emergency Assistant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(emergency.router, prefix="/emergency", tags=["emergency"])
app.include_router(location.router, prefix="/location", tags=["location"])


@app.get("/")
async def health_check():
    return {"status": "ok", "service": "EEGA backend"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

