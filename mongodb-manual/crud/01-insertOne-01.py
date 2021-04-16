#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client.MyMongoManualPy

id = db.inventory.insert_one(
  {"item": "canvas",
   "qty": 100,
   "tags": ["cotton"],
   "size": {"h": 28, "w": 35.5, "uom": "cm"}}
)

cursor = db.inventory.find({"item": "canvas"})
pprint.pprint(list(cursor)[:3])
