from datetime import datetime
from pydantic import BaseModel, Field


class OrmBaseModel(BaseModel):
    class Config:
        from_attributes = True

class PetModel(OrmBaseModel):
    name: str
    type_pet: str
    age: int
    # owner_name: str 
    # created_at: datetime|None = Field(default=datetime.utcnow())

class PetUpdate(OrmBaseModel):
    id : int
    name:str
    age:int
    type_pet:str


class UsersResponse(OrmBaseModel):
    name: str
    lastname: str
    phone_number: int|None


class UserInDB(UsersResponse):
    password:str

class TokenResponse(BaseModel):
    access_token: str

class UserSignup(OrmBaseModel):
    name: str
    lastname: str
    password: str = Field(min_length=10)
    # phone_number: int|None

class UserSuccesReg(BaseModel):
    successful : UserSignup

class UserLogin(OrmBaseModel):
    login: UsersResponse

class TokenResponse(BaseModel):
    token: str