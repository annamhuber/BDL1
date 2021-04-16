#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['mongodb-examples']

# SELECT state, SUM(pop) AS totalPop
# FROM zipcodes
# GROUP BY state
# HAVING totalPop >= (10*1000*1000)

cursor = db.zipcodes.aggregate( [
   { "$group": { "_id": "$state", "totalPop": { "$sum": "$pop" } } },
   { "$match": { "totalPop": { "$gte": 10*1000*1000 } } }
] )

for doc in cursor:
    pprint.pprint(doc)
