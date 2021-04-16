#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['mflix']

for d in db.movies.find({"cast": {"$exists": True}}).limit(3):
    pprint.pprint(d)

print("~"*30, "\n")
for d in db.movies.find({"cast.2": {"$exists": True}}).limit(2):
    pprint.pprint(d)

print("~"*30, "\n")
for d in db.movies.find({"cast.1": "Zane Grey"}).limit(2):
    pprint.pprint(d)

print("~"*30, "\n")
for d in db.movies.find({"cast":
                         {"$in": ["Zane Grey", "Bruno"]}
                        }).limit(2):
    pprint.pprint(d)
