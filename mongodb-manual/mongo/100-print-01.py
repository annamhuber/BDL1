#!/usr/bin/env python3
from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost")
db = client['mongodb-examples']

for d in db.restaurants.find({}).limit(5):
  print(d)

print("~"*30, "\n")

for d in db.restaurants.find({}).limit(5):
  pprint(d)

print("~"*30, "\n")

cursor = db.restaurants.find({}).limit(5)
for d in cursor:
  pprint(d)
