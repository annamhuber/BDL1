#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['mflix']

# :-((
s = 0
for d in db.movies.find({"viewerRating": {"$gt": 5.2},
                         "viewerVotes": {"$exists": True}
                        }):
    s += d['viewerVotes']
print(s)

# :-((
print("~"*30, "\n")
s = sum(d['viewerVotes'] for d in
        db.movies.find({ "viewerRating" : {"$gt": 5.2},
                         "viewerVotes": {"$exists": True}
                       })
       )
print(s)

print("~"*30, "\n")


# projection
# https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find
for d in db.movies.find({ "viewerRating" : {"$gt": 5.2},
                          "viewerVotes": {"$exists": True}
                        },
                        {"viewerVotes": 1} ).limit(5):
    pprint.pprint(d)

print("~"*30, "\n")

# :-(
s = sum(d['viewerVotes'] for d in
        db.movies.find({ "viewerRating" : {"$gt": 5.2},
                         "viewerVotes": {"$exists": True}
                       },
                       {"viewerVotes": 1} ))
pprint.pprint(s)

# :-)
pipeline = [
    {"$project": {"_id": 0, "viewerRating": 1, "viewerVotes": 1}},
    # {"$match": {
    #     "viewerRating": {
    #         "$gt": 5.2}, "viewerVotes": {"$exists": True}}},
    # {"$group": {"_id": "Total", "sumVotes": {"$sum": "$viewerVotes"}}},
    {"$limit": 10},
]

for doc in db.movies.aggregate(pipeline):
    pprint.pprint(doc)
