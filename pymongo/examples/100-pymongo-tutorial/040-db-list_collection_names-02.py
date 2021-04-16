#!/usr/bin/env python3
from pymongo import MongoClient

client = MongoClient("mongodb://localhost")
print(client.mflix.list_collection_names())
