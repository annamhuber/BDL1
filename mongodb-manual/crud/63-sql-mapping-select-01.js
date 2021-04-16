db = db.getSiblingDB('MyMongoManual');

// SELECT * FROM people
db.people.find()

// SELECT id, user_id, status FROM people
db.people.find(
    { },
    { user_id: 1, status: 1 }
)

// SELECT user_id, status FROM people
db.people.find(
    { },
    { user_id: 1, status: 1, _id: 0 }
)

// SELECT * FROM people WHERE status = "A"
db.people.find(
    { status: "A" }
)

// SELECT user_id, status FROM people WHERE status = "A"
db.people.find(
    { status: "A" },
    { user_id: 1, status: 1, _id: 0 }
)

// SELECT * FROM people WHERE status != "A"
db.people.find(
    { status: { $ne: "A" } }
)

// SELECT * FROM people WHERE status = "A" AND age = 50
db.people.find(
    { status: "A",
      age: 50 }
)

// SELECT * FROM people WHERE status = "A" OR age = 50
db.people.find(
    { $or: [ { status: "A" } , { age: 50 } ] }
)

// SELECT * FROM people WHERE age > 25
db.people.find(
    { age: { $gt: 25 } }
)

// SELECT * FROM people WHERE age < 25
db.people.find(
   { age: { $lt: 25 } }
)

// SELECT * FROM people WHERE age > 25 AND age <= 50
db.people.find(
   { age: { $gt: 25, $lte: 50 } }
)

// SELECT * FROM people WHERE user_id like "%bc%"
db.people.find( { user_id: /bc/ } )
// -or-
db.people.find( { user_id: { $regex: /bc/ } } )

// SELECT * FROM people WHERE user_id like "bc%"
db.people.find( { user_id: /^bc/ } )
// -or-
db.people.find( { user_id: { $regex: /^bc/ } } )

// SELECT * FROM people WHERE status = "A" ORDER BY user_id ASC
db.people.find( { status: "A" } ).sort( { user_id: 1 } )

// SELECT * FROM people WHERE status = "A" ORDER BY user_id DESC
db.people.find( { status: "A" } ).sort( { user_id: -1 } )

// SELECT COUNT(*) FROM people
db.people.count()
// or
db.people.find().count()

// SELECT COUNT(user_id) FROM people
db.people.count( { user_id: { $exists: true } } )
// or
db.people.find( { user_id: { $exists: true } } ).count()

// SELECT COUNT(*) FROM people WHERE age > 30
db.people.count( { age: { $gt: 30 } } )
// or
db.people.find( { age: { $gt: 30 } } ).count()

// SELECT DISTINCT(status) FROM people
db.people.aggregate( [ { $group : { _id : "$status" } } ] )
// or, for distinct value sets that do not exceed the BSON size limit
db.people.distinct( "status" )

// SELECT * FROM people LIMIT 1
db.people.findOne()
// or
db.people.find().limit(1)

// SELECT * FROM people LIMIT 5 SKIP 10
db.people.find().limit(5).skip(10)

// EXPLAIN SELECT * FROM people WHERE status = "A"
db.people.find( { status: "A" } ).explain()
