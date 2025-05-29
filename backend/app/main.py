from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class HazardReport(BaseModel):
    lat: float
    lon: float
    description: str
    photo_url: str | None = None

@app.get("/health")      # simple liveness probe
async def health():
    return {"status": "ok"}

@app.post("/report")
async def create_report(report: HazardReport):
    # TODO: call Open311 endpoint here
    return {"queued": True, "detail": report.dict()}
