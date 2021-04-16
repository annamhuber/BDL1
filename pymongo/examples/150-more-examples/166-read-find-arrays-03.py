#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['mflix']

for d in db.movies_with_reviews.find().limit(3):
    pprint.pprint(d)

print("~"*30, "\n")

for d in db.movies_with_reviews.find({"reviews.0.email":
                                      "Destany89@hotmail.com"}).limit(3):
    pprint.pprint(d)

print("~"*30, "\n")

for d in db.movies_with_reviews.find({"reviews":
                                      {"$elemMatch": {
                                        "email":
                                        "Joannie.Bartoletti36@gmail.com"}
                                      }
                                     }).limit(3):
    pprint.pprint(d)
