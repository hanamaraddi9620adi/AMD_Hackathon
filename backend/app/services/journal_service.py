from sqlalchemy.orm import Session

from app.models.journal import Journal
from app.models.user import User

from app.repositories.journal_repository import (
    journal_repository,
)


class JournalService:
    """
    Business logic for Trading Journal.
    """

    def create_journal(
        self,
        db: Session,
        current_user: User,
        symbol: str,
        exchange: str,
        trade_type: str,
        action: str,
        quantity: int,
        entry_price: float,
        exit_price: float,
        trade_date,
        title: str,
        strategy: str,
        emotion: str,
        confidence: float,
        content: str,
        lessons: str,
    ):

        pnl = 0.0
        profitable = False

        if exit_price > 0:
            if action.upper() == "BUY":
                pnl = (exit_price - entry_price) * quantity
            else:
                pnl = (entry_price - exit_price) * quantity

            profitable = pnl > 0

        journal = Journal(
            user_id=current_user.id,
            symbol=symbol.upper(),
            exchange=exchange.upper(),
            trade_type=trade_type,
            action=action.upper(),
            quantity=quantity,
            entry_price=entry_price,
            exit_price=exit_price,
            pnl=pnl,
            trade_date=trade_date,
            title=title,
            strategy=strategy,
            emotion=emotion,
            confidence=confidence,
            content=content,
            lessons=lessons,
            ai_feedback="",
            is_profitable=profitable,
        )

        return journal_repository.create(
            db,
            journal,
        )

    def get_all_journals(
        self,
        db: Session,
        current_user: User,
    ):

        return journal_repository.get_all_by_user(
            db,
            current_user.id,
        )

    def update_journal(
        self,
        db: Session,
        current_user: User,
        journal_id: str,
        exit_price: float | None,
        pnl: float | None,
        emotion: str | None,
        confidence: float | None,
        content: str | None,
        lessons: str | None,
        ai_feedback: str | None,
        is_profitable: bool | None,
    ):

        journal = journal_repository.get_by_id(
            db,
            journal_id,
        )

        if (
            journal is None
            or journal.user_id != current_user.id
        ):
            raise ValueError(
                "Journal entry not found."
            )

        if exit_price is not None:
            journal.exit_price = exit_price

        if pnl is not None:
            journal.pnl = pnl

        if emotion is not None:
            journal.emotion = emotion

        if confidence is not None:
            journal.confidence = confidence

        if content is not None:
            journal.content = content

        if lessons is not None:
            journal.lessons = lessons

        if ai_feedback is not None:
            journal.ai_feedback = ai_feedback

        if is_profitable is not None:
            journal.is_profitable = is_profitable

        return journal_repository.update(
            db,
            journal,
        )

    def delete_journal(
        self,
        db: Session,
        current_user: User,
        journal_id: str,
    ):

        journal = journal_repository.get_by_id(
            db,
            journal_id,
        )

        if (
            journal is None
            or journal.user_id != current_user.id
        ):
            raise ValueError(
                "Journal entry not found."
            )

        journal_repository.delete(
            db,
            journal,
        )

        return {
            "message": "Journal entry deleted successfully."
        }


journal_service = JournalService()