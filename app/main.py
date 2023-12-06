from fastapi import FastAPI, APIRouter
from sqlalchemy.orm import Session
from db.database import Pet, session
from datetime import datetime
from routes import router as router_pets
from routes_users import router_users


app = FastAPI(title="Pets simple project")
app.include_router(router= router_pets)
app.include_router(router=router_users)


@app.get("/start", tags=["start"])
async def get_started():
    return {"hello":"welcome"}

