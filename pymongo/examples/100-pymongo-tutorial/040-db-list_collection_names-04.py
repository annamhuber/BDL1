#!/usr/bin/env python3
import pymongo

client = pymongo.MongoClient("mongodb://localhost")
#db = client.mongodb-examples
db = client['mongodb-examples']
print(db.list_collection_names())
