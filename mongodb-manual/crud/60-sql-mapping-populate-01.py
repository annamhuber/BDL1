#!/usr/bin/env python3
import pymongo

client = pymongo.MongoClient("mongodb://localhost")
db = client.people

db.people.delete_many({})

from bson.objectid import ObjectId
id = db.people.insert_one(
  {
    "_id": ObjectId("509a8fb2f3f4948bd2f983a0"),
    "user_id": "abc123",
    "age": 55,
    "status": 'A'
  }
)
