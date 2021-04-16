db = db.getSiblingDB('MyMongoManual');

db.categories_ancestors.deleteMany({})

db.categories_ancestors.insertMany(
  [
      { _id: "MongoDB"
        , ancestors: [ "Books", "Programming", "Databases" ]
        , parent: "Databases" }
    , { _id: "dbm"
        , ancestors: [ "Books", "Programming", "Databases" ]
        , parent: "Databases" }
    , { _id: "Databases"
        , ancestors: [ "Books", "Programming" ]
        , parent: "Programming" }
    , { _id: "Languages"
        , ancestors: [ "Books", "Programming" ]
        , parent: "Programming" }
    , { _id: "Programming"
        , ancestors: [ "Books" ]
        , parent: "Books" }
    , { _id: "Books"
        , ancestors: [ ]
        , parent: null }
  ]
);
