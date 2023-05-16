import datetime
from typing import List, Optional, Union
from pydantic import BaseModel

class UserSchema(BaseModel):
    id = int
    userId = str 
    name = str 
    email = str 
    phone = str 
    description = str 
    firstName = str 
    lastName = str
    position = str 
#    created = datetime.date
#    updated = datetime.date
#   lastLogged = datetime.date
#    isEnabled = bool
    leaderId = str 
    organization = str 
    agentGuid = str 

#    user_owner = list[AgentSchema] = []

class VehicleSchema(BaseModel):
    id = int
    number = str
    simnumber1 = str
    imei = str
    deviceTypeId = int
    modelId = str
    IdVehicle = str
    vehicleId = int
    agentGuid = str

#    vehicle_owner = list[AgentSchema] = []

class AgentSchema(BaseModel):
    id = int
    agentId = str 
    accINN = str
    accKPP = str 
    accAddress = str 
    accFullName = str
    name = str 
    # blocked = bool
    # created = datetime.date
    # updated = datetime.date
    #
#    users = list[UserSchema]
#    vehicles = list[VehicleSchema]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

