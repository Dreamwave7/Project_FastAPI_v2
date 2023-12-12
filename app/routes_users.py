from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter
from requests import Session
from db.database import get_db
from auth import *

router_users = APIRouter(prefix="/auth", tags=["users"])


@router_users.post("/signup")
async def signup(db:Annotated[Session, Depends(get_db)], body:str):
    res = db.query(Users).where(Users.name == body).first()
    return res
    
    # signup = await signup_user(body,db)
    # return signup
