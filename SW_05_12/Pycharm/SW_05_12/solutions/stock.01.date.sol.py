#!/usr/bin/env python3
from pymongo import MongoClient

client = MongoClient("mongodb://localhost")
database = client.socratica
data = database.google_stock_data

limit = 50

# https://docs.mongodb.com/manual/reference/operator/aggregation/
# https://docs.mongodb.com/manual/reference/operator/aggregation/dateFromString

data.aggregate([
    {"$addFields": {
        "Date2": {"$dateFromString": {"dateString": "$Date"}},
    }},
    {"$limit": limit},
    {"$out": "fixed"}
])

#
# {
#     "_id" : ObjectId("5f31379f6fde9ee9044f78fc"),
#     "Date" : "8/19/2014",
#     "Open" : 585.002622,
#     "High" : 587.342658,
#     "Low" : 584.002627,
#     "Close" : 586.862643,
#     "Volume" : 978600,
#     "Adj Close" : 586.862643,
#     "Date2" : ISODate("2014-08-19T00:00:00.000Z")
# }
