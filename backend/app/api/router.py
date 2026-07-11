from fastapi import APIRouter

from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.portfolio import router as portfolio_router
from app.api.v1.endpoints.journal import router as journal_router
from app.api.v1.endpoints.market import router as market_router
from app.api.v1.endpoints.chat import router as chat_router
from app.api.test_auth import router as test_router
from app.api.v1.endpoints.analyze import router as analyze_router




api_router = APIRouter()





api_router.include_router(auth_router)
api_router.include_router(portfolio_router)
api_router.include_router(journal_router)
api_router.include_router(market_router)
api_router.include_router(chat_router)
api_router.include_router(test_router)
api_router.include_router(analyze_router)