
from sqlalchemy import Column,Integer,String,func, Boolean, ForeignKey
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
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    name = Column(String(length=20), nullable=False)
    age = Column(Integer, nullable=False)
    type_pet = Column(String, nullable=False)
    created_at = Column(DateTime, nullable= True)

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=30), nullable= False)
    lastname = Column(String(length=30), nullable= False)
    phone_number = Column(Integer,nullable=True)
    is_active = Column(Boolean, default=False)
    password = Column(String(length=500), nullable=False)
    test = Column(String, nullable=True)



async def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()




# Base.metadata.create_all(bind=engine)  #проверка