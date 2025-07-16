# backend/schemas/planner.py

from pydantic import BaseModel, Field
from typing import List

class PlannerRequest(BaseModel):
    user_story: str = Field(..., example="As a user, I want to upload a profile picture.")

class PlannerResponse(BaseModel):
    tasks: List[str]
