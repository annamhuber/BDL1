db = db.getSiblingDB('myNewDB');

db.users.insertMany(
  [
      { name: "jane", joined: ISODate("2011-03-02"), age: 42
        , status: "A", likes: ["golf", "racquetball"] }
    , { name: "joe" , joined: ISODate("2011-03-02"), age: 24
        , status: "B", likes: ["tennis", "golf", "swimming"] }
    , { name: "sue" , joined: ISODate("2011-04-01"), age: 28
        , status: "B", likes: [ "tennis", "basketball" ] }
    , { name: "marc", joined: ISODate("2010-02-15"), age: 50
        , status: "A", likes: [ "soccer" ] }
  ]
);
