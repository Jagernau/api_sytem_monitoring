import models
from database import SessionLocal, Base, engine
import config
from requests_func import login_gln, get_gln_json
from sqlalchemy import update

gln_login = config.LOGIN["gln_login"]
frt_login = config.LOGIN["frt_login"]

gln_password = config.PASSWORD["gln_password"]
frt_password = config.PASSWORD["frt_password"]

gln_domain = config.DOMAI_NAME["gln_domain"]
frt_domain = config.DOMAI_NAME["frt_domain"]

gln_views = ["agents", "users", "vehicles",]


token = login_gln(gln_domain, login=gln_login, password=gln_password)



db = SessionLocal()
Base.metadata.create_all(bind=engine)


gln_agents = get_gln_json(token, gln_domain, "agents")
#agents
if gln_agents is not None:
    for i in gln_agents:
        if "80eb1587-12cf-44d4-b0d0-c09b7ddf6110" in i["id"]:
            continue

        if i["id"] == db.query(models.Agent).filter_by(agentId=i["id"]).first().agentId:
            db.execute(update(models.Agent).where(models.Agent.agentId==i["id"]).values(

                accINN = i["client"]["accINN"],
                accKPP = i["client"]["accKPP"],
                accAddress = i["client"]["accAddress"],
                accFullName = i["client"]["accFullName"],
                name = i["name"],
                blocked = i["blocked"],
                created = i["created"],
            ))
            db.commit()

        else:

            place_in_db = models.Agent(
                        agentId = i["id"],
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

gln_users = get_gln_json(token, gln_domain, "users")
#user
if gln_users is not None:
    for i in gln_users:
        if "80eb1587-12cf-44d4-b0d0-c09b7ddf6110" in i["agentGuid"]:
            continue
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

gln_vehicles = get_gln_json(token, gln_domain, "vehicles")
#vehicle
if gln_vehicles is not None:
    for i in gln_vehicles:
        if "80eb1587-12cf-44d4-b0d0-c09b7ddf6110" in i["owner"]:
            continue
        if "simnumber1" in i:
            sim = i["simnumber1"]
        else:
            sim = None
        place_in_db = models.Vehicle(

            number = i["number"],
            simnumber1 = sim,
            imei = i["imei"],
            modelId = i["modelId"],

            IdVehicle = i["id"], #"000000-0000-0000-0000000000"

            vehicleId = i["vehicleId"], #000000
            deviceTypeId = i["deviceTypeId"],
            agentGuid = i["owner"],
        )
        db.add(place_in_db)

    db.commit()
db.close()
