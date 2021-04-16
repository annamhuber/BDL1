db = db.getSiblingDB('MyMongoManual');

db.categories_path.deleteMany({})

db.categories_path.insertMany(
  [
      { _id: "Books", path: null }
    , { _id: "Programming", path: ",Books," }
    , { _id: "Databases", path: ",Books,Programming," }
    , { _id: "Languages", path: ",Books,Programming," }
    , { _id: "MongoDB", path: ",Books,Programming,Databases," }
    , { _id: "dbm", path: ",Books,Programming,Databases," }
  ]
);
