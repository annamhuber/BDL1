#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['mflix']

for doc in db.movies.aggregate([
    {"$project": {"plot": 0, "_id": 0} },
    { "$limit": 5 } ]):
  pprint.pprint(doc)

print("~"*30, "\n")

for doc in db.movies.aggregate([
    {"$project": {"plot": 0, "_id": 0} },
    {"$match": {"cast": {"$exists" : True}}},
    {"$addFields": {"castCnt" : {"$size": "$cast"}} },
    {"$limit": 5 } ] ):
  pprint.pprint(doc)
