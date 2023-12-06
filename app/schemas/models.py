from datetime import datetime
from pydantic import BaseModel, Field



class OrmBaseModel(BaseModel):
    class Config:
        from_attributes = True

class PetModel(OrmBaseModel):
    name: str
    type_pet: str
    age: int
    owner_name: str 
    # created_at: datetime|None = Field(default=datetime.utcnow())

class PetUpdate(OrmBaseModel):
    id : int
    name:str
    age:int
    type_pet:str




