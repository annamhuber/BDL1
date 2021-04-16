db = db.getSiblingDB('mongodb-examples');

 db.zipcodes.aggregate( [
  { $group: { _id: "$state", totalPop: { $sum: "$pop" } } },
]);


// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// $out
 db.zipcodes.aggregate( [
  { $group: { _id: "$state", totalPop: { $sum: "$pop" } } },
  { $out: "last_results" }
]);

db.last_results.find().limit(3).pretty()
