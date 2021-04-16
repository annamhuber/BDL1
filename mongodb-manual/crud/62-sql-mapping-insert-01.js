db = db.getSiblingDB('MyMongoManual');

// INSERT INTO people(user_id,
//                   age,
//                   status)
// VALUES ("bcd001",
//         45,
//         "A")
db.people.insertOne(
   { user_id: "bcd001", age: 45, status: "A" }
)
