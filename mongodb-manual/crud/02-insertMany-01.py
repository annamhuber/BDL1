#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client.MyMongoManualPy

db.inventory.insert_many([
  {"item": "journal",
   "qty": 25,
   "tags": ["blank", "red"],
   "size": {"h": 14, "w": 21, "uom": "cm"}},
  {"item": "mat",
   "qty": 85,
   "tags": ["gray"],
   "size": {"h": 27.9, "w": 35.5, "uom": "cm"}},
  {"item": "mousepad",
   "qty": 25,
   "tags": ["gel", "blue"],
   "size": {"h": 19, "w": 22.85, "uom": "cm"}}
])

cursor = db.inventory.find()
pprint.pprint(list(cursor)[:3])
