db = db.getSiblingDB('MyMongoManual');

// CREATE TABLE people (
//     id MEDIUMINT NOT NULL AUTO_INCREMENT,
//     user_id Varchar(30),
//     age Number,
//     status char(1),
//     PRIMARY KEY (id)
// )
db.people.insertOne( {
  user_id: "abc123",
  age: 55,
  status: "A"
} )

db.createCollection("people")


// ALTER TABLE people ADD join_date DATETIME
db.people.updateMany(
  { },
  { $set: { join_date: new Date() } }
)


// ALTER TABLE people DROP COLUMN join_date
db.people.updateMany(
  { },
  { $unset: { "join_date": "" } }
)


// CREATE INDEX idx_user_id_asc ON people(user_id)
db.people.createIndex( { user_id: 1 } )


// CREATE INDEX idx_user_id_asc_age_desc
//   ON people(user_id, age DESC)
db.people.createIndex( { user_id: 1, age: -1 } )


// DROP TABLE people
db.people.drop()
