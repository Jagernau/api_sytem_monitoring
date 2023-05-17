import datetime
from os import listdir
from typing import List, Optional, Union
from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int | None
    userId: str
    name: str | None
    email: str | None
    phone: str | None
    description: str | None
    firstName: str | None
    lastName: str | None
    position: str | None
    created: datetime.date
    updated: datetime.date
    lastLogged: datetime.date
    isEnabled: bool
    leaderId: str | None
    organization: str | None
    agentGuid: str | None

    user_owner = list = []

class VehicleSchema(BaseModel):
    id: int
    number: str | None
    simnumber1: str | None
    imei: str | None
    deviceTypeId: int | None
    modelId: str | None
    IdVehicle: str | None
    vehicleId: int | None
    agentGuid: str | None

    vehicle_owner = list = []

class AgentSchema(BaseModel):
    id: int
    agentId: str | None
    accINN: str | None
    accKPP: str | None
    accAddress: str | None
    accFullName: str | None
    name: str | None
    blocked: bool
    created: datetime.date
    updated: datetime.date

    users: list = []
    vehicles: list = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

