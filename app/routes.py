from typing import List
from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db, Pet
from schemas.responses import *
from schemas import models
from queries import *
import auth
router = APIRouter(prefix="/pet",tags=["animals"])

@router.get("/get_pets", response_model=List[PetResponse], response_model_exclude_none=True)
async def get_pets(db:Annotated[Session, Depends(get_db)],user = Depends(auth.get_current_user)):
    result = await get_all_pets(db, user)
    return result

@router.get("/get_pet/{id}", response_model=PetResponse|None)
async def get_pet(id:int, db:Annotated[Session, Depends(get_db)],user = Depends(auth.get_current_user)):
    result = await get_pet_from_id(db, pet_id=id, user = user)
    return result

@router.post("/create_pet", response_model=PetResponse)
async def create_pet(data: PetModel, db:Annotated[Session,Depends(get_db)], user = Depends(auth.get_current_user)):
    new_pet = await create_pet_from_data(db,data,user)
    return new_pet

@router.patch("/edit_pet")
async def edit_pet(data:PetUpdate, db:Annotated[Session, Depends(get_db)], user = Depends(auth.get_current_user)):
    update_pet = await update_pet_from_data(db, data, user)
    return update_pet


@router.delete("/delete_pet/{id}")
async def delete_pet(id:int, db:Annotated[Session, Depends(get_db)], user = Depends(auth.get_current_user)):
    removing = await delete_pet_from_id(db, id, user)
    return removing

@router.get("/all_cats", response_model=List[PetResponse])
async def get_cats(db:Annotated[Session, Depends(get_db)], user = Depends(auth.get_current_user)):
    cats = await get_all_cats(db,user)
    return cats

@router.get("/all_dogs", response_model=List[PetResponse])
async def get_dogs(db:Annotated[Session, Depends(get_db)], user = Depends(auth.get_current_user)):
    dogs = await get_all_dogs(db,user)
    return dogs