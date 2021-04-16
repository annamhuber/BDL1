#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['dbkoda-SampleCollections']

for d in db.crunchbase_database.find().limit(2):
    pprint.pprint(d)

print("~"*30, "\n")
for d in db.crunchbase_database.find({"offices.3": {"$exists": True},
                                      "offices": {"$elemMatch":
                                                  {"state_code": "NJ"}}},
                                     {"overview": 0,
                                      "relationships": 0,
                                      "screenshots": 0}).limit(1):
    pprint.pprint(d)
