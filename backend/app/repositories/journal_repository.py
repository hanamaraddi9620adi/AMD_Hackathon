from sqlalchemy.orm import Session

from app.models.journal import Journal


class JournalRepository:
    """
    Repository layer responsible for all
    Journal database operations.
    """

    def create(
        self,
        db: Session,
        journal: Journal,
    ) -> Journal:

        db.add(journal)
        db.commit()
        db.refresh(journal)

        return journal

    def get_all_by_user(
        self,
        db: Session,
        user_id: str,
    ) -> list[Journal]:

        return (
            db.query(Journal)
            .filter(Journal.user_id == user_id)
            .order_by(Journal.created_at.desc())
            .all()
        )

    def get_by_id(
        self,
        db: Session,
        journal_id: str,
    ) -> Journal | None:

        return (
            db.query(Journal)
            .filter(Journal.id == journal_id)
            .first()
        )

    def update(
        self,
        db: Session,
        journal: Journal,
    ) -> Journal:

        db.commit()
        db.refresh(journal)

        return journal

    def delete(
        self,
        db: Session,
        journal: Journal,
    ) -> None:

        db.delete(journal)
        db.commit()


journal_repository = JournalRepository()