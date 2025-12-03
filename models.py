from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)


class Calculation(Base):
    __tablename__ = "calculations"
    
    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, nullable=False)  # "c2" или "soliyev"
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    result = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
