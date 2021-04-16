db = db.getSiblingDB('myNewDB');

db.users.aggregate(
  [
    { $project : { month_joined : { $month : "$joined" } } } ,
    { $group : { _id : {month_joined:"$month_joined"}
                 , number : { $sum : 1 } } },
    { $sort : { "_id.month_joined" : 1 } }
  ]
)
