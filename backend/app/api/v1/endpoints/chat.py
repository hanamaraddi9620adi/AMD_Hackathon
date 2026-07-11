from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.database.sessions import get_db
from app.models.user import User
from app.agents.orchestrator import orchestrator
from app.schemas.chat_schema import ChatRequest

router = APIRouter(
    prefix="/chat",
    tags=["AI Analysis"],
)


@router.post("/analyze")
def analyze(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return orchestrator.analyze(
        db=db,
        current_user=current_user,
        symbol=request.query,
    )