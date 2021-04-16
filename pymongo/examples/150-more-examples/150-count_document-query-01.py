#!/usr/bin/env python3
import pymongo

client = pymongo.MongoClient("mongodb://localhost")
db = client['mflix']

print(db.movies.count_documents({"year": {"$gt": 1999}}))

print("~"*30, "\n")
print(db.movies.count_documents({"year": 1997}))
print(db.movies.count_documents({"year": 1998}))
print(db.movies.count_documents({"year": 1999}))
print(db.movies.count_documents({"year": {"$gte": 1997, "$lte": 1999} }))
print(db.movies.count_documents({"year": {"$in": [1997,1998,1999]}}))

print("~"*30, "\n")
# :-((
# https://docs.python.org/3/library/stdtypes.html#dict
print(db.movies.count_documents({"year":
                                 {"$eq": 1997, "$eq": 1998, "$eq": 1999} }))
print(db.movies.count_documents({"year":
                                 {"$eq": 1999, "$eq": 1998, "$eq": 1997} }))
print({"foo": 24, "foo": 42})


print("~"*30, "\n")
# :-/
print([{"foo": 24}, {"foo": 42}])
print(db.movies.count_documents({"$or":
                                 [ {"year": 1997},
                                   {"year": 1998},
                                   {"year": 1999} ]
                                }))

print("~"*30, "\n")
print(list(range(1997,2000)))
# :-|
print(db.movies.count_documents({"year": {"$in": list(range(1997,2000))} }))
# :-)
print(db.movies.count_documents({"year": {"$gte": 1997, "$lte": 1999} }))

print("~"*30, "\n")
print(db.movies.count_documents({"year": {"$eq": 1997  } }))
print(db.movies.count_documents({"year": {"$eq": "1997"} }))
