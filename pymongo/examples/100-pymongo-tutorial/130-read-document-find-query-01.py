#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['mflix']


for d in db.movies.find({"viewerRating" : {"$gt": 5.2} }).limit(2):
  pprint.pprint(d)

print("~"*30, "\n")

for d in db.movies.find({"viewerRating" : {"$gt": 5.2} }
                       ).sort("viewerRating").limit(2):
  pprint.pprint(d)

print("~"*30, "\n")

for d in db.movies.find({"viewerRating" : {"$gt": 5.2} }
                       ).sort("viewerRating", -1).limit(2):
  pprint.pprint(d)

print("~"*30, "\n")

for d in db.movies.find(
    {"year": 1999, "viewerRating" : {"$gt": 5.2} }).limit(2):
  pprint.pprint(d)
