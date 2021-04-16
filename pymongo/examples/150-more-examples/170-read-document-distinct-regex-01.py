#!/usr/bin/env python3
import pymongo
import pprint

client = pymongo.MongoClient("mongodb://localhost")
db = client['mflix']

print(db.theaters.distinct("location.address.state"))

print("~"*30, "\n")
count = len(db.theaters.distinct("location.address.state"))
print(count)

print("~"*30, "\n")
print(len(db.movies.distinct("language")))
print(db.movies.distinct("language")[:10])

print("~"*30, "\n")
print(db.movies.distinct("language", {"language": "German"}))
print(db.movies.find({"language": "German"}).count())

print("~"*30, "\n")
print(len(db.movies.distinct("language", {"language":
                                          {"$regex": "^German"}})))

print(db.movies.distinct("language", {"language":
                                      {"$regex": "^German"}})[:10])

print("~"*30, "\n")
print(db.movies.distinct("language", {"language":
                                      {"$regex": "German"}})[:10])

print("~"*30, "\n")
# https://api.mongodb.com/python/current/api/bson/regex.html#bson.regex.Regex
from bson.regex import Regex
print(db.movies.distinct("language", {"language": Regex("^German") })[:10])
