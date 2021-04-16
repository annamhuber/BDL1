db = db.getSiblingDB('mongodb-examples');


db.zipcodes.aggregate( [
  { $group:
    {
      _id: { state: "$state", city: "$city" },
      pop: { $sum: "$pop" }
    }
  },
  { $sort: { pop: 1 } },
  { $group:
    {
      _id : "$_id.state",
      biggestCity:  { $last: "$_id.city" },
      biggestPop:   { $last: "$pop" },
      smallestCity: { $first: "$_id.city" },
      smallestPop:  { $first: "$pop" }
    }
  },

] );
