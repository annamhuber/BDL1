db = db.getSiblingDB('MyMongoManual');

db.inventory.deleteMany({});

db.inventory.insertMany([
  { _id: 1, item: null },
  { _id: 2 }
])
