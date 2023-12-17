from db.database import get_db
from sqlalchemy.orm import Session
from db.database import Pet
from schemas.models import *
from datetime import datetime
from sqlalchemy import and_, update, values
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



async def update_pet_from_data(db:Session, data:PetUpdate, user:UserInDB):
    # query = update(Pet).where(Pet.id == data.id).values(data.model_dump())
    query = update(Pet).where(and_(Pet.id == data.id, Pet.owner_id == user.id)).values(data.model_dump())
    updated_pet = db.execute(query)
    db.commit()

    return updated_pet

async def delete_pet_from_id(db:Session, id_pet: int, user:UserInDB):
    query = db.query(Pet).where(and_(Pet.id == id_pet, Pet.owner_id == user.id)).first()
    if query:
        removing = db.delete(query)
        db.commit()
        return {"Success": f"Pet with id {id_pet} was deleted"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pet doesnt exist")
    


async def get_all_cats(db:Session, user:UserInDB):
    # query = db.query(Pet).where(and_(Pet.type_pet.in_(["Cat","cat","CAT"], Pet.owner_id == user.id))).all()
    query = db.query(Pet).filter(Pet.type_pet.in_(["Cat","cat","CAT"])).where(Pet.owner_id == user.id).all()
    if query:
        return query
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Doesnt exist any cat")

async def get_all_dogs(db:Session, user:UserInDB):
    query = db.query(Pet).filter(Pet.type_pet.in_(["DOG","Dog","dog"])).where(Pet.owner_id == user.id).all()
    if query:
        return query
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Doesnt exist any dog")


    



































