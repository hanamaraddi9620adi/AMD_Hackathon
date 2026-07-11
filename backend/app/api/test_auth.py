from fastapi import APIRouter
from fastapi import Depends

from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/test",
    tags=["Test"],
)


@router.get("/me")
def me(
    current_user: User = Depends(get_current_user),
):
    return {
        "id": current_user.id,
        "name": current_user.full_name,
        "email": current_user.email,
    }