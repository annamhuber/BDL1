#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client.MyMongoManualPy

for d in db.inventory.find({"item": None}):
  pprint.pprint(d)

for d in db.inventory.find({"item": {"$type": 10}}):
  pprint.pprint(d)

for d in db.inventory.find({"item": {"$exists": False}}):
  pprint.pprint(d)
