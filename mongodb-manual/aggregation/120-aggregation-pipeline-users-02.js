db = db.getSiblingDB('myNewDB');

db.users.aggregate(
  [
    { $project : { name:{$toUpper:"$name"} , _id:0 } },
    { $sort : { name : 1 } }
  ]
)
