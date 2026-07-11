from sqlalchemy.orm import Session

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)

from app.models.user import User
from app.repositories.user_repository import user_repository


class AuthService:

    def signup(
        self,
        db: Session,
        full_name: str,
        email: str,
        password: str,
    ):

        print("=" * 60)
        print("SIGNUP REQUEST")
        print("Email:", email)

        existing = user_repository.get_user_by_email(
            db,
            email,
        )

        if existing:
            print("User already exists")
            raise ValueError("User already exists")

        hashed = hash_password(password)

        print("Password hashed successfully")

        user = User(
            full_name=full_name,
            email=email,
            hashed_password=hashed,
        )

        created = user_repository.create_user(
            db,
            user,
        )

        print("User inserted into database")

        token = create_access_token(
            {
                "sub": created.email,
            }
        )

        print("JWT created")
        print("=" * 60)

        return {
            "id": created.id,
            "full_name": created.full_name,
            "email": created.email,
            "access_token": token,
            "token_type": "bearer",
        }

    def login(
        self,
        db: Session,
        email: str,
        password: str,
    ):

        print("=" * 60)
        print("LOGIN REQUEST")
        print("EMAIL:", email)

        user = user_repository.get_user_by_email(
            db,
            email,
        )

        print("USER FOUND:", user is not None)

        if not user:
            print("FAILED -> USER NOT FOUND")
            print("=" * 60)
            raise ValueError("Invalid credentials")

        print("Stored Hash:")
        print(user.hashed_password)

        valid = verify_password(
            password,
            user.hashed_password,
        )

        print("PASSWORD VALID:", valid)

        if not valid:
            print("FAILED -> PASSWORD MISMATCH")
            print("=" * 60)
            raise ValueError("Invalid credentials")

        token = create_access_token(
            {
                "sub": user.email,
            }
        )

        print("LOGIN SUCCESS")
        print("=" * 60)

        return {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "access_token": token,
            "token_type": "bearer",
        }


auth_service = AuthService()