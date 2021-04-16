#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['mflix']

print(db.movies.find_one())
print("~"*30, "\n")
pprint.pprint(db.movies.find_one())

print("~"*30, "\n")
pprint.pprint(db.movies.find_one({}))

print("~"*30, "\n")
pprint.pprint(db.movies.find_one({"year": 1999}))

print("~"*30, "\n")
pprint.pprint(db.movies.find_one({"year": 2099}))

print("~"*30, "\n")
# https://docs.python.org/3.7/library/stdtypes.html?#dict.keys
pprint.pprint(db.movies.find_one({"year": 1999}).keys())

print("~"*30, "\n")
pprint.pprint(db.movies.find_one({"year": 1999}).values())
