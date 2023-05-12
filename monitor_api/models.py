from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class Agent(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True, autoincrement=True)
    agentId = Column(String, unique=True) #"0000-0000-0000-0000-00000000000"
    accINN = Column(String, nullable=True) 
    accKPP = Column(String, nullable=True)
    accAddress = Column(String, nullable=True)
    accFullName = Column(String, nullable=True)
    name = Column(String, nullable=True)
    blocked = Column(Boolean, default=False)
    created = Column(DateTime, nullable=True)
    updated = Column(DateTime, nullable=True)

    users = relationship("User", back_populates="user_owner")
    vehicles = relationship("Vehicle", back_populates="")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(String, unique=True) #"0000-0000-0000-0000-00000000000"
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    description = Column(String, nullable=True)
    firstName = Column(String, nullable=True)
    lastName = Column(String, nullable=True)
    position = Column(String, nullable=True)
    created = Column(DateTime, nullable=True)
    updated = Column(DateTime, nullable=True)
    lastLogged = Column(DateTime, nullable=True)
    isEnabled = Column(Boolean, default=True)
    leaderId = Column(String, nullable=True)
    organization = Column(String, nullable=True)
    agentGuid = Column(String, ForeignKey('agents.agentId'))

    user_owner = relationship("Agent", back_populates="users")

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String)
    simnumber1 = Column(String)
    imei = Column(String)
    device_type_id = Column(Integer)
    model_id = Column(String)

    agentGuid = Column(String, ForeignKey('agents.agentId'))

    vehicle_owner = relationship("Agent", back_populates="vehicles")
