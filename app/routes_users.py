from typing import Annotated

from fastapi import Depends, APIRouter


router_users = APIRouter(prefix="/auth", tags=["users"])
