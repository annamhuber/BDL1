#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['mflix']

for d in db.movies.find().limit(2):
    pprint.pprint(d)

print("~"*30, "\n")

for d in db.movies.find({}, {"title": 1}).limit(4):
    pprint.pprint(d)

print("~"*30, "\n")

for d in db.movies.find({}, {"title": 1, "_id": 0}).limit(4):
    pprint.pprint(d)

print("~"*30, "\n")

for d in db.movies.find({}, {"title": 1, "year": 1,"_id": 0}).limit(4):
    pprint.pprint(d)

print("~"*30, "\n")

for d in db.movies.find({}, ["title", "genre"]).limit(4):
    pprint.pprint(d)

print("~"*30, "\n")
