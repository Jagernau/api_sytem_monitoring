from sqlalchemy.orm import Session
from models import User, Agent, Vehicle

#Agent
def get_agent_from_name(db: Session, name: str):
    return db.query(Agent).filter(Agent.name == name).first()

def get_all_agents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Agent).offset(skip).limit(limit).all()

#User
def get_user_from_name(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()

def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

#Vehicle
def get_vehicle_from_name(db: Session, name: str):
    return db.query(Vehicle).filter(Vehicle.name == name).first()

def get_all_vehicles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Vehicle).offset(skip).limit(limit).all()


