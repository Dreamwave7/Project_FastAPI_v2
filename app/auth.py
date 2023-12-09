from typing import Annotated
from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from db.database import *
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

oauth = OAuth2PasswordBearer()


SECRET_KEY = "9d25e094faa6c9d25e094faa6ca2556c818166b7a9563a2556c818166b7a9563"
ALGM = "HS256"

bcrypt = CryptContext(schemes=["HS256"])

async def hash_password(password:str):
    hashed_password = bcrypt.hash(password)
    return hash_password


async def verify_password(ordinary_password:str,hashed_password:str):
    result = bcrypt.verify(ordinary_password, hashed_password)
    return result

async def get_user(db:Session, username:str):
    query = db.query(Users).where(Users.name == username).first()
    result = db.execute(query)
    if result:
        return result
    return None

async def authenticate_user(db:Session, username:str, password:str):
    user = await get_user(db, username)
    user: Users
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    
    return user

async def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp" : expire})
    encoded_token = jwt.encode(to_encode, SECRET_KEY, ALGM)
    return encoded_token

async def get_current_user(token:Annotated[str,Depends(oauth)], db:Session = Depends(get_db)):
    excption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Cant validate user")
    data = jwt.decode(token, SECRET_KEY,algorithms=[ALGM])
    username = data.get("sub")

    if username is None:
        raise excption
    
    user = get_user(db,username)
    if user is None:
        raise excption
    
    return user

    

    
    
