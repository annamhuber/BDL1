#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['mongodb-examples']

cursor = db.zipcodes.aggregate( [
   { "$group": { "_id":
                 { "state": "$state",
                   "city": "$city" },
                 "pop": { "$sum": "$pop" } } },
   { "$group": { "_id": "$_id.state",
                 "avgCityPop": { "$avg": "$pop" } } }
] )

for doc in cursor:
    pprint.pprint(doc)
