#!/usr/bin/env python3
# 2020-10, Bruno Grossniklaus, https://github.com/it-gro

import pymongo
# import pprint

# https://pymongo.readthedocs.io/en/stable/api/pymongo/cursor.html#pymongo.cursor.Cursor.batch_size
# https://pymongo.readthedocs.io/en/stable/api/pymongo/cursor.html#pymongo.cursor.Cursor.retrieved

client = pymongo.MongoClient("mongodb://localhost")
db = client['mflix']

cursor = db.movies.find({}, {"title": 1, "_id": 0})
# cursor.batch_size(1000)

# pprint.pprint(cursor.explain())
# print(cursor.cursor_id)

i = 0
for d in cursor:
    print("loop: %d, cursor.retrieved: %d, doc: %s" % (i, cursor.retrieved, d))
    i += 1
    if i >= 5000:
        break

cursor.close()
