from pydantic import NonNegativeFloat
from monitor_api import models
from monitor_api.database import SessionLocal, Base, engine
import config
from requests_func import login_gln, get_gln_json


gln_login = config.LOGIN["gln_login"]
frt_login = config.LOGIN["frt_login"]

gln_password = config.PASSWORD["gln_password"]
frt_password = config.PASSWORD["frt_password"]

gln_domain = config.DOMAI_NAME["gln_domain"]
frt_domain = config.DOMAI_NAME["frt_domain"]

gln_views = ["agents", "users", "vehicles",]
frt_views = []


token = login_gln(gln_domain, login=gln_login, password=gln_password)

name_view = "agents"

gln_data = get_gln_json(token, gln_domain, name_view)


db = SessionLocal()
Base.metadata.create_all(bind=engine)

#agents
if gln_data is not None:
    for i in gln_data:
        if "00000000" in i["client"]["agentId"]:
            check_agentId = i["client"]["id"]
        else:
            check_agentId = i["client"]["agentId"]
        place_in_db = models.Agent(
                    agentId = check_agentId,
                    accINN = i["client"]["accINN"],
                    accKPP = i["client"]["accKPP"],
                    accAddress = i["client"]["accAddress"],
                    accFullName = i["client"]["accFullName"],
                    name = i["name"],
                    blocked = i["blocked"],
                    created = i["created"],
                    updated = i["updated"],
        )
        db.add(place_in_db)

    db.commit()

#user
if gln_data is not None:
    for i in gln_data:
        place_in_db = models.User(

            userId = i["id"], #"0000-0000-0000-0000-00000000000"
            name = i["name"],
            email = i["email"],
            phone = i["phone"],
            description = i["description"],
            firstName = i["firstName"],
            lastName = i["lastName"],
            position = i["lastName"],
            created = i["created"],
            updated = i["updated"],
            lastLogged = i["lastLogged"],
            isEnabled = i["isEnabled"],
            leaderId = i["leaderId"],
            organization = i["organization"],
            agentGuid = i["agentGuid"],
        )
        db.add(place_in_db)

    db.commit()

#vehicle
if gln_data is not None:
    for i in gln_data:
        place_in_db = models.Vehicle(

            number = i["number"],
            simnumber1 = i["simnumber"],
            imei = i["imei"],
            deviceTypeId = i["deviceTypeId"],
            modelId = i["model"],
            vehicleId = i["id"],
            deviceTypeId = i["deviceTypeId"],
            agentGuid = i["agentGuid"],
        )
        db.add(place_in_db)

    db.commit()


db.close()
