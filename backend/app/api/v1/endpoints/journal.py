from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.database.sessions import get_db

from app.models.user import User

from app.schemas.journal_schema import (
    JournalCreate,
    JournalUpdate,
    JournalResponse,
)

from app.services.journal_service import (
    journal_service,
)

router = APIRouter(
    prefix="/journal",
    tags=["Journal"],
)


@router.post(
    "/",
    response_model=JournalResponse,
)
def create_journal(
    request: JournalCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    try:

        return journal_service.create_journal(
            db=db,
            current_user=current_user,
            symbol=request.symbol,
            exchange=request.exchange,
            trade_type=request.trade_type,
            action=request.action,
            quantity=request.quantity,
            entry_price=request.entry_price,
            exit_price=request.exit_price,
            trade_date=request.trade_date,
            title=request.title,
            strategy=request.strategy,
            emotion=request.emotion,
            confidence=request.confidence,
            content=request.content,
            lessons=request.lessons,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "/",
    response_model=list[JournalResponse],
)
def get_journals(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return journal_service.get_all_journals(
        db=db,
        current_user=current_user,
    )


@router.put(
    "/{journal_id}",
    response_model=JournalResponse,
)
def update_journal(
    journal_id: str,
    request: JournalUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    try:

        return journal_service.update_journal(
            db=db,
            current_user=current_user,
            journal_id=journal_id,
            exit_price=request.exit_price,
            pnl=request.pnl,
            emotion=request.emotion,
            confidence=request.confidence,
            content=request.content,
            lessons=request.lessons,
            ai_feedback=request.ai_feedback,
            is_profitable=request.is_profitable,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.delete(
    "/{journal_id}",
)
def delete_journal(
    journal_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    try:

        return journal_service.delete_journal(
            db=db,
            current_user=current_user,
            journal_id=journal_id,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )