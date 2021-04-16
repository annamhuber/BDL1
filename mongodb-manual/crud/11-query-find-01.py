#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client.MyMongoManualPy

# SELECT * FROM inventory
for d in db.inventory.find(): pprint.pprint(d)

# SELECT * FROM inventory WHERE status = "D"
for d in db.inventory.find({"status": "D"}):
  pprint.pprint(d)

# SELECT * FROM inventory WHERE status in ("A", "D")
for d in db.inventory.find({"status": {"$in": ["A", "D"]}}):
  pprint.pprint(d)

# SELECT * FROM inventory WHERE status = "A" AND qty < 30
for d in db.inventory.find({"status": "A", "qty": {"$lt": 30}}):
  pprint.pprint(d)

# SELECT * FROM inventory WHERE status = "A" OR qty < 30
for d in db.inventory.find(
    {"$or": [{"status": "A"}, {"qty": {"$lt": 30}}]}):
  pprint.pprint(d)

# SELECT * FROM inventory WHERE status = "A"
#                           AND ( qty < 30 OR item LIKE "p%")
for d in db.inventory.find({
    "status": "A",
    "$or": [{"qty": {"$lt": 30}}, {"item": {"$regex": "^p"}}]}):
  pprint.pprint(d)
