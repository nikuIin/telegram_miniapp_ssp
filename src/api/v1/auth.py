from fastapi import APIRouter, Request, Response, HTTPException
from pydantic import BaseModel
from hmac import HMAC
from core.config import TELEGRAM_API_TOKEN

router = APIRouter(prefix="/v1/auth", tags=["auth"])


@router.post("/signin")
async def login(request: Request):
    print(request.body)
    return request.body
