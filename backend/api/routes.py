# backend/api/routes.py

from fastapi import APIRouter, HTTPException
from backend.schemas.planner import PlannerRequest, PlannerResponse
from agents.planner import PlannerAgent

router = APIRouter()
planner_agent = PlannerAgent()  # singleton instance

@router.post("/", response_model=PlannerResponse)
def generate_tasks(request: PlannerRequest):
    try:
        tasks = planner_agent.predict(request.user_story)
        if not tasks:
            raise HTTPException(status_code=400, detail="No tasks generated.")
        return PlannerResponse(tasks=tasks)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PlannerAgent failed: {str(e)}")
