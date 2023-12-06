from .models import OrmBaseModel
from datetime import datetime

class PetResponse(OrmBaseModel):
    id: int
    name: str
    type_pet: str
    age: int
    owner_name: str 
    created_at: datetime|None
    