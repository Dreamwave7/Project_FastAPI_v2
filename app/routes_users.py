from typing import Annotated

from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer

router_users = APIRouter(prefix="/auth", tags=["users"])

auth2 = OAuth2PasswordBearer(tokenUrl="login")

@router_users.get("/test")
async def read_test(token:Annotated[str, Depends(auth2)]):
    return {"token":token}