from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    def create_user(
        self,
        db: Session,
        user: User,
    ) -> User:

        db.add(user)

        db.commit()

        db.refresh(user)

        return user

    def get_user_by_email(
        self,
        db: Session,
        email: str,
    ) -> User | None:

        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    def get_user_by_id(
        self,
        db: Session,
        user_id: str,
    ) -> User | None:

        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    def update_user(
        self,
        db: Session,
        user: User,
    ) -> User:

        db.commit()

        db.refresh(user)

        return user

    def delete_user(
        self,
        db: Session,
        user: User,
    ):

        db.delete(user)

        db.commit()


user_repository = UserRepository()