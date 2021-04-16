#!/usr/bin/env python3
from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost")
database = client["mflix"]
collection = database["movies"]

query = {
  "$or": [
    {
      "director": "Gernot Bock-Stieber"
    }, {
      "year": 1999,
      "runtime": {"$gt": 190},
      "viewerRating": {"$exists": True}
    }
  ],
  "genre": {"$ne": ""}
}


projection = {
  "director": 1,
  "genre": 1,
  "runtime": 1,
  "title": 1,
  "viewerRating": 1,
  "viewerVotes": 1,
  "year": 1,
  "_id": 0
}

sort = [("runtime", 1),("year", 1)]
limit=5
skip=0

cursor = collection.find(filter=query,
                         projection=projection,
                         sort=sort,
                         limit=limit,
                         skip=skip)

try:
    for doc in cursor:
        pprint.pprint(doc)
finally:
    cursor.close()
