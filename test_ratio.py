# from fuzzywuzzy import fuzz
#
# string1 = "Баранов Сергей Владимирович"
# string2 = "Баранов_С_В__ИП"
#
# ratio = fuzz.ratio(string1, string2)
#
# print(ratio)

from database import SessionLocal, Base, engine
import models

db = SessionLocal()

# agents = db.query(models.Agent).all()
# count = []
# for i in agents:
#     count.append(len(i.users))
#
# print(sorted(count))

a = db.query(models.Agent).filter_by(agentId="d79d8b0a-f77c-4c7d-b4dd-41663c140781").first().vehicles
for i in a:
    if "пере" in i.number:
        continue
    else:
        print(i.number)
