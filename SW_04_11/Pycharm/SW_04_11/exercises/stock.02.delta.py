#!/usr/bin/env python3
from pymongo import MongoClient

client = MongoClient("mongodb://localhost")
database = client.socratica
data = database.google_stock_data

limit = 50

# delta: abs(High - Low) round 2 digits

for doc in data.aggregate([
        {"$project": {
            "delta": {
                # ***
            },
            "_id": 0,
            "Open": 1,
            "High": 1,
            "Low": 1,
            "Close": 1,
            "Volume": 1,
        }
        },
        {"$match": {   # delta >= 40 or Volume >= 70000000
            # ***
            # ***
            # ***
            # ***
        }},
        {"$sort": None},  # *** delta descending
        {"$limit": limit},
]):
    print(doc)


# {'Open': 755.541298, 'High': 759.421272, 'Low': 676.001158, 'Close': 695.001219, 'Volume': 24977900, 'delta': 83.42}
# {'Open': 393.20067, 'High': 397.540676, 'Low': 338.510572, 'Close': 362.620635, 'Volume': 79170700, 'delta': 59.03}
# {'Open': 734.60125, 'High': 734.891274, 'Low': 677.181165, 'Close': 693.841184, 'Volume': 33148100, 'delta': 57.71}
