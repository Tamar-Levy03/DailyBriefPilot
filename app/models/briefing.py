from pydantic import BaseModel

class BriefingResponse(BaseModel):
    message: str