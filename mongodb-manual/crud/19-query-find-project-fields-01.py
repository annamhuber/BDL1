#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client.MyMongoManualPy

# SELECT * from inventory WHERE status = "A"
for d in db.inventory.find({"status": "A"}):
  pprint.pprint(d)

# SELECT _id, item, status from inventory WHERE status = "A"
for d in db.inventory.find(
    {"status": "A"}, {"item": 1, "status": 1}):
  pprint.pprint(d)

# SELECT item, status from inventory WHERE status = "A"
for d in db.inventory.find(
    {"status": "A"}, {"item": 1, "status": 1, "_id": 0}):
  pprint.pprint(d)

for d in db.inventory.find(
    {"status": "A"}, {"status": 0, "instock": 0}):
  pprint.pprint(d)

for d in db.inventory.find(
    {"status": "A"}, {"item": 1, "status": 1, "size.uom": 1}):
  pprint.pprint(d)

for d in db.inventory.find({"status": "A"}, {"size.uom": 0}):
  pprint.pprint(d)

for d in db.inventory.find(
    {"status": "A"}, {"item": 1, "status": 1, "instock.qty": 1}):
  pprint.pprint(d)

for d in db.inventory.find(
    {"status": "A"},
    {"item": 1, "status": 1, "instock": {"$slice": -1}}):
  pprint.pprint(d)
