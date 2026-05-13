from fastapi import FastAPI

app = FastAPI(title="DailyBriefPilot API", version="1.0")


@app.get("/health")
def health_check():
    return {"status": "working"}

@app.post("/generate-brief")
def generate_brief():
    # Placeholder for the actual implementation of the brief generation logic
    return {"brief": "Taily briefing is being prepared..."}
