#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['mongodb-examples']

group1   = { "$group":
             {
               "_id": { "state": "$state", "city": "$city" },
               "pop": { "$sum": "$pop" }
             }}
sort     = {"$sort": { "pop": 1 } }
group2   = { "$group":
             {
               "_id" : "$_id.state",
               "biggestCity":  { "$last": "$_id.city" },
               "biggestPop":   { "$last": "$pop" },
               "smallestCity": { "$first": "$_id.city" },
               "smallestPop":  { "$first": "$pop" }
             }}
project     = { "$project":
                { "_id": 0,
                  "state": "$_id",
                  "biggestCity":  { "name": "$biggestCity",
                                    "pop": "$biggestPop" },
                  "smallestCity": { "name": "$smallestCity",
                                    "pop": "$smallestPop" }
                }}
limit = { "$limit": 10}

#pipeline = [group1, sort]
#pipeline = [group1, sort, group2]
pipeline = [group1, sort, group2, project, limit]
#pipeline = [group1, sort, group2, project]

pprint.pprint(pipeline)
print("~"*30, "\n")

for doc in db.zipcodes.aggregate(pipeline):
    pprint.pprint(doc)
