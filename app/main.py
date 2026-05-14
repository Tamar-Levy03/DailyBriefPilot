from fastapi import FastAPI
from app.models.briefing import BriefingResponse
from app.services.briefing_service import BriefingService

app = FastAPI(title="DailyBriefPilot API", version="1.0")


@app.get("/health")
def health_check():
    return {"status": "working"}

@app.post("/generate-brief")
async def generate_brief():
    # Placeholder for the actual implementation of the brief generation logic
    briefing_service = BriefingService()
    message = await briefing_service.generate_briefing()
    print(message)
    return BriefingResponse(message=message)