#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client.MyMongoManualPy

for d in db.inventory.find({"tags": ["red", "blank"]}):
  pprint.pprint(d)

for d in b.inventory.find({"tags": {"$all": ["red", "blank"]}}):
  pprint.pprint(d)

for d in db.inventory.find({"tags": "red"}):
  pprint.pprint(d)

for d in  db.inventory.find({"dim_cm": {"$gt": 25}}):
  pprint.pprint(d)

for d in db.inventory.find({"dim_cm": {"$gt": 15, "$lt": 20}}):
  pprint.pprint(d)

for d in  db.inventory.find({"dim_cm":
                             {"$elemMatch": {"$gt": 22, "$lt": 30}}}):
  pprint.pprint(d)

for d in  db.inventory.find({"dim_cm.1": {"$gt": 25}}):
  pprint.pprint(d)

for d in  db.inventory.find({"tags": {"$size": 3}}):
  pprint.pprint(d)
