db = db.getSiblingDB('MyMongoManual');

db.people.deleteMany({});

db.people.insertOne(
  {
    _id: ObjectId("509a8fb2f3f4948bd2f983a0"),
    user_id: "abc123",
    age: 55,
    status: 'A'
  }
)
