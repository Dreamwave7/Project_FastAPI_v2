from db.database import get_db
from sqlalchemy.orm import Session
from db.database import Pet
from schemas.models import *
from datetime import datetime
from sqlalchemy import update, values
from fastapi import HTTPException, status



async def get_all_pets(db:Session, user:UserInDB):
    result = db.query(Pet).where(Pet.owner_id == user.id).all()
    return result

async def get_pet_from_id(db:Session, pet_id:int, user: UserInDB):
    result = db.query(Pet).where(Pet.owner_id == user.id).where(Pet.id == pet_id).first()
    if result:
        return result
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This id doesnt exist")

async def create_pet_from_data(db:Session, data:PetModel, user:UserInDB):
    new_pet = Pet(**data.model_dump(),
                  created_at = datetime.utcnow().date(),
                  owner_id = user.id,
                  owner_name = user.name)
    db.add(new_pet)
    db.commit()
    db.refresh(new_pet)
    return new_pet



async def update_pet_from_data(db:Session, data:PetUpdate):
    query = update(Pet).where(Pet.id == data.id).values(data.model_dump())
    updated_pet = db.execute(query)
    # current_pet = db.query(Pet).where(Pet.id == data.id).first()
    db.commit()
    # db.refresh(current_pet)

    return query

async def delete_pet_from_id(db:Session, id_pet: int):
    query = db.query(Pet).where(Pet.id == id_pet).first()
    if query:
        removing = db.delete(query)
        db.commit()
        return {"pet was deleted": id_pet}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pet doesnt exist")
    


async def get_all_cats(db:Session):
    query = db.query(Pet).where(Pet.type_pet.in_(["Cat","cat","CAT"])).all()
    if query:
        return query
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Doesnt exist any cat")

async def get_all_dogs(db:Session):
    query = db.query(Pet).where(Pet.type_pet.in_(["Dog","DOG","dog"])).all()
    if query:
        return query
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Doesnt exist any dog")


    



































