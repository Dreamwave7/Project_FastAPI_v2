from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter, HTTPException, status
from requests import Session
from db.database import get_db
from auth import *

router_users = APIRouter(prefix="/auth", tags=["users"])


@router_users.post("/signup", response_model=UserSuccesReg)
async def signup(db:Annotated[Session, Depends(get_db)], data:UserSignup):
    check_user = get_user(db, data.name)
    if check_user is None:
        signup = await signup_user(data,db)
        return {"successful": data}
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This username already exist!")
    
@router_users.post("/login",response_model=TokenResponse)
async def login(db : Annotated[Session, Depends(get_db)], data = Depends(OAuth2PasswordRequestForm)):
    username = data.username
    user = authenticate_user(db, username=data.username, password = data.password)
    token = await create_access_token(data = {"sub":username})
    return {"token":token}



@router_users.post("/check_token")
async def check_token(user:Users = Depends(get_current_user)):
    print(user.id, user.lastname)


