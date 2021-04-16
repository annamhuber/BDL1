#!/usr/bin/env python3
import pymongo

client = pymongo.MongoClient("mongodb://localhost")
db = client.MyMongoManualPy

db.inventory.delete_many({})

db.inventory.insert_many([{"_id": 1, "item": None},
                          {"_id": 2}])
