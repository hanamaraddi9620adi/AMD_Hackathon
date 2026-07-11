from pydantic import BaseModel


class ChatRequest(BaseModel):
    query: str


class ChatResponse(BaseModel):
    market: dict
    technical: dict
    news: dict
    sentiment: dict
    risk: dict
    portfolio: dict
    analysis: dict