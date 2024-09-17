from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    company = Column(String)
    manager_id = Column(Integer, ForeignKey('users.id'))
    manager = relationship('User', remote_side=[id])

class AccessLog(Base):
    __tablename__ = 'access'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('users.id'))
    access_time = Column(DateTime)
    direction = Column(String)  
    gate_id = Column(Integer)
    gate_name = Column(String)

