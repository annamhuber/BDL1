#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['mflix']

for d in db.theaters.find().limit(3):
    pprint.pprint(d)

print("~"*30, "\n")
for d in db.theaters.find({"location.address.state": "CA"}).limit(3):
    pprint.pprint(d)

print("~"*30, "\n")
for d in db.theaters.find({"location.address.state": "CA"}
                          , {"location.geo": 1
                             , "_id": 0}).limit(3):
    pprint.pprint(d)

print("~"*30, "\n")
for d in db.theaters.find({"location.address.state": "CA"}
                          , {"location.geo.coordinates": 1
                             , "_id": 0}).limit(3):
    pprint.pprint(d)

print("~"*30, "\n")
for d in db.theaters.find({"location.address.state": "CA",
                           "location.geo.coordinates.0": {
                             "$gte": -117.96, "$lte": -117.90} },
                          {"location.geo.coordinates": 1,
                           "_id": 0}).limit(3):
    pprint.pprint(d)
