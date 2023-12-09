from passlib.context import CryptContext
import jwt
from datetime import datetime
from db.database import *
from sqlalchemy.orm import Session



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



