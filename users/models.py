from .database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String)
    password = Column(String)
    phone = Column(String)
    rewards = Column(Integer)
    role = Column(String)
    member_type = Column(String)
    hotel_id = Column(Integer)