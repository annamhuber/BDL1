#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['mflix']

for doc in db.reviews.aggregate([
    { "$limit": 2 } ]):
  pprint.pprint(doc)

print("~"*30, "\n")

for doc in db.reviews.aggregate([
    {"$lookup": {
      "from" : "movies",
      "localField": "movie_id",
      "foreignField": "_id",
      "as": "movie"}},
    {"$project": {"text": 0,
                  "movie.plot": 0 } },
    {"$limit": 2 } ] ):
  pprint.pprint(doc)
