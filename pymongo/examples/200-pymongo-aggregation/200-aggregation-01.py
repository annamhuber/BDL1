#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['mflix']

for d in db.movies.find().limit(2):
    pprint.pprint(d)

print("~" * 30, "\n")

for doc in db.movies.aggregate([{"$match": {"year": 1999}}, {"$limit": 2}]):
    pprint.pprint(doc)

print("~" * 30, "\n")

project = {"$project": {"title": 1,
                        "genre": 1,
                        "viewerVotes": 1,
                        "viewerRating": 1,
                        "_id": 0}}
match = {"$match": {"viewerVotes": {"$gte": 1000},
                    "runtime": {"$gte": 150}}}
sort = {"$sort": {"year": -1, "viewerVotes": -1}}
limit = {"$limit": 5}
skip = {"$skip": 1000}
pipeline = [match, project, skip, sort, limit]

pprint.pprint(pipeline)

print("~" * 30, "\n")

for doc in db.movies.aggregate(pipeline):
    pprint.pprint(doc)
