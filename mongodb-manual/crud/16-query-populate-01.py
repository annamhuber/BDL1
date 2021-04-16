#!/usr/bin/env python3
import pymongo

client = pymongo.MongoClient("mongodb://localhost")
db = client.MyMongoManualPy

db.inventory.delete_many({})

db.inventory.insert_many([
  {"item": "journal",
   "instock": [
     {"warehouse": "A", "qty": 5},
     {"warehouse": "C", "qty": 15}]},
  {"item": "notebook",
   "instock": [
     {"warehouse": "C", "qty": 5}]},
  {"item": "paper",
   "instock": [
     {"warehouse": "A", "qty": 60},
     {"warehouse": "B", "qty": 15}]},
  {"item": "planner",
   "instock": [
     {"warehouse": "A", "qty": 40},
     {"warehouse": "B", "qty": 5}]},
  {"item": "postcard",
   "instock": [
     {"warehouse": "B", "qty": 15},
     {"warehouse": "C", "qty": 35}]},
])
