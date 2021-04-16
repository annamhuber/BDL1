db = db.getSiblingDB('MyMongoManual');

// DELETE FROM people WHERE status = "D"
db.people.deleteMany( { status: "D" } )

// DELETE FROM people
db.people.deleteMany({})
