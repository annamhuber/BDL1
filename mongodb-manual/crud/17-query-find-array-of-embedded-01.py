#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client.MyMongoManualPy

for d in db.inventory.find({"instock": {"warehouse": "A",
                                        "qty": 5}}):
    pprint.pprint(d)

for d in db.inventory.find({"instock": {"qty": 5,
                                        "warehouse": "A"}}):
    pprint.pprint(d)

for d in db.inventory.find({'instock.qty': {"$lte": 20}}):
    pprint.pprint(d)

for d in db.inventory.find({'instock.0.qty': {"$lte": 20}}):
    pprint.pprint(d)

for d in db.inventory.find({"instock":
                            {"$elemMatch": {"qty": 5,
                                            "warehouse": "A"}}}):
    pprint.pprint(d)

for d in db.inventory.find({"instock": {"$elemMatch":
                                        {"qty": {"$gt": 10,
                                                 "$lte": 20}}}}):
    pprint.pprint(d)

for d in db.inventory.find({"instock.qty": {"$gt": 10,
                                            "$lte": 20}}):
    pprint.pprint(d)

for d in db.inventory.find({"instock.qty": 5,
                            "instock.warehouse": "A"}):
    pprint.pprint(d)
