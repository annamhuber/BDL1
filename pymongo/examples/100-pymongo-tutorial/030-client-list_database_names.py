#!/usr/bin/env python3
import pymongo

client = pymongo.MongoClient("mongodb://localhost")
print(client.list_database_names())
