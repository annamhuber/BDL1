#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['mongodb-examples']

cursor = db.zipcodes.aggregate( [
  { "$group": { "_id": "$state",
                "popSum": { "$sum": "$pop" },
                "popAvg": { "$avg": "$pop" },
                "popMin": { "$min": "$pop" },
                "popMax": { "$max": "$pop" },
                "popCnt": { "$sum": 1 }} },
  { "$match": { "popSum": { "$gte": 10*1000*1000 } } },
  { "$limit": 5 }
  ] )

for doc in cursor:
    pprint.pprint(doc)

print("~"*30, "\n")

cursor = db.zipcodes.aggregate( [
  { "$match": { "pop": {"$gte": 1000} } },
  { "$group": { "_id": "$state",
                "popSum": { "$sum": "$pop" },
                "popAvg": { "$avg": "$pop" },
                "popMin": { "$min": "$pop" },
                "popMax": { "$max": "$pop" },
                "popCnt": { "$sum": 1 }} },
  { "$match": { "popSum": { "$gte": 10*1000*1000 } } },
  { "$limit": 5 }
  ] )

for doc in cursor:
    pprint.pprint(doc)
