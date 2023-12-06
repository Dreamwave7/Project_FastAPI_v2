
from sqlalchemy import Column,Integer,String,func
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_URL = "postgresql://iewxjyrk:xN0ZGT8TtA7QnSIT9ms76lXYnuywZv9m@flora.db.elephantsql.com/iewxjyrk"
engine = create_engine(DB_URL)

Session = sessionmaker(autoflush=False, autocommit = False, bind=engine)

session = Session()

Base = declarative_base()



class Pet(Base):
    __tablename__ = "pets"
    id = Column(Integer, primary_key=True, nullable=False)
    owner_name = Column(String(length=25), nullable= False)
    name = Column(String(length=20), nullable=False)
    age = Column(Integer, nullable=False)
    type_pet = Column(String, nullable=False)
    created_at = Column(DateTime, nullable= True)



async def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()




# Base.metadata.create_all(bind=engine)  #проверка