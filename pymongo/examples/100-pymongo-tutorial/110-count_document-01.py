#!/usr/bin/env python3
import pymongo

client = pymongo.MongoClient("mongodb://localhost")
db = client['mflix']

# :-)    # data stays on server
print(db.movies.count_documents({"year": 1999}))

print("~"*30, "\n")

# https://docs.python.org/3.7/library/stdtypes.html?#list
# https://docs.python.org/3.7/library/stdtypes.html?#sequence-types-list-tuple-range
# :-((    # data is on client (network, ram)
data=list(db.movies.find({"year": 1999}))
print(len(data))
