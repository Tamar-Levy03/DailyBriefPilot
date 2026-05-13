from fastapi import FastAPI
from app.models.briefing import BriefingResponse

app = FastAPI(title="DailyBriefPilot API", version="1.0")


@app.get("/health")
def health_check():
    return {"status": "working"}

@app.post("/generate-brief")
def generate_brief():
    # Placeholder for the actual implementation of the brief generation logic
    return BriefingResponse(message="Your daily briefing is being prepared...")
