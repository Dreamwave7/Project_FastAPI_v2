from typing import Annotated
from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from db.database import *
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from schemas.models import *

oauth = OAuth2PasswordBearer(tokenUrl="/auth/login")


SECRET_KEY = "9d25e094faa6c9d25e094faa6ca2556c818166b7a9563a2556c818166b7a9563"
ALGM = "HS256"

bcrypt = CryptContext(schemes=["bcrypt"], deprecated = "auto")

async def hash_password(password:str):
    return bcrypt.hash(password)


def verify_password(ordinary_password:str,hashed_password:str):
    result = bcrypt.verify(ordinary_password, hashed_password)
    return result

def get_user(db:Session, username:str):
    query = db.query(Users).filter(Users.name == username).first()
    # res = db.execute(query)
    if query:
        return query
    return None

def authenticate_user(db:Session, username:str, password:str):
    excption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Cant validate user")
    user = get_user(db, username)
    user: Users
    if not user:
        raise excption
    if not  verify_password(password, user.password):
        raise excption
    
    return user

async def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=3000)
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

async def signup_user(data:UserSignup, db: Annotated[Session, Depends(get_db)]):
    encoded_password = await hash_password(data.password)
    new_user = Users(**data.model_dump(exclude="password"),password = encoded_password)
    db.add(new_user)
    db.commit()
    return new_user
    

    
    
