#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client.MyMongoManualPy

for d in db.inventory.find({"size": {"h": 14,
                                     "w": 21, "uom": "cm"}}):
    pprint.pprint(d)

for d in db.inventory.find({"size": {"w": 21,
                                     "h": 14, "uom": "cm"}}):
    pprint.pprint(d)

for d in db.inventory.find({"size.uom": "in"}):
    pprint.pprint(d)

for d in db.inventory.find({"size.h": {"$lt": 15}}):
    pprint.pprint(d)

for d in db.inventory.find({"size.h": {"$lt": 15},
                            "size.uom": "in", "status": "D"}):
    pprint.pprint(d)
