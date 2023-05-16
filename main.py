from fastapi import FastAPI, HTTPException, Query
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
import uvicorn


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

@app.get("/agents/", response_model=list[AgentSchema])
def all_agents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    agents = crud.get_all_agents(db, skip=skip, limit=limit)
    return agents

@app.get("/vehicles/", response_model=list[VehicleSchema])
def all_vehicles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    agents = crud.get_all_vehicles(db, skip=skip, limit=limit)
    return agents



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

