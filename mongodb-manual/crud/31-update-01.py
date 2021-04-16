#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client.MyMongoManualPy

db.inventory.update_one(
  {"item": "paper"},
  {"$set": {"size.uom": "cm", "status": "P"},
   "$currentDate": {"lastModified": True}}
)

db.inventory.update_many(
  {"qty": {"$lt": 50}},
  {"$set": {"size.uom": "in", "status": "P"},
   "$currentDate": {"lastModified": True}}
)

db.inventory.replace_one(
  {"item": "paper"},
  {"item": "paper",
   "instock": [
     {"warehouse": "A", "qty": 60},
     {"warehouse": "B", "qty": 40}]}
)
