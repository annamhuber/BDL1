db = db.getSiblingDB('MyMongoManual');

// UPDATE people SET status = "C" WHERE age > 25
db.people.updateMany(
  { age: { $gt: 25 } },
  { $set: { status: "C" } }
)

// UPDATE people SET age = age + 3 WHERE status = "A"
db.people.updateMany(
  { status: "A" } ,
  { $inc: { age: 3 } }
)
