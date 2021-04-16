db = db.getSiblingDB('myNewDB');

db.users.aggregate(
  [
    { $project :
      {
        month_joined : { $month : "$joined" },
        name : 1,
        _id : 0
      }
    },
    { $sort : { month_joined : 1 } }
  ]
)
