from fastapi import FastAPI, HTTPException, Query
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
import uvicorn
from transliterate import translit

from models import Base
from schemas  import AgentSchema, UserSchema, VehicleSchema
import crud


Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()

#agents
@app.get("/agents/", response_model=list[AgentSchema])
def all_agents(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    agents = crud.get_all_agents(db, skip=skip, limit=limit)
    return agents

@app.get("/agents/{agent_name}", response_model=AgentSchema)
def get_agent_by_name(agent_name: str, db: Session = Depends(get_db)):
    db_agent = crud.get_agent_from_name(db, name=agent_name)
    if db_agent is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_agent


#vehicle
@app.get("/vehicles/", response_model=list[VehicleSchema])
def all_vehicles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    agents = crud.get_all_vehicles(db, skip=skip, limit=limit)
    return agents



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

