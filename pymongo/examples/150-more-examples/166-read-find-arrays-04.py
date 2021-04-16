#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['mflix']

#for d in db.movieDetails.find().limit(3):
#  pprint.pprint(d)

print("~"*30, "\n")
for d in db.movieDetails.find({"countries": "Switzerland",
                               "genres": "Drama"},
                              {"title": 1, "year": 1,
                               "countries": 1, "genres": 1,
                               "_id": 0}).limit(5):
    pprint.pprint(d)
