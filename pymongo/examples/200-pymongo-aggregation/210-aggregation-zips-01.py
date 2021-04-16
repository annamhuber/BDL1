#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['mongodb-examples']

for d in db.zipcodes.find().limit(2):
  pprint.pprint(d)
