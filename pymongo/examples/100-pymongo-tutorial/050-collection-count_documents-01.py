#!/usr/bin/env python3
import pymongo

client = pymongo.MongoClient("mongodb://localhost")
db = client['mflix']

#print(db.movies.count_documents())
print(db.movies.count_documents({}))
print(db['movies'].count_documents({}))
