#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['mflix']

l = 0
for d in db.movies.find({"year": 1999}):
  l+=1
  if l > 2: break
  pprint.pprint(d)

print("~"*30, "\n")

for d in db.movies.find({"year": 1999}).limit(2):
  pprint.pprint(d)
