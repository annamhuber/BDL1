db = db.getSiblingDB('myNewDB');

// SELECT cust_id,
//        count(*)
// FROM orders
// GROUP BY cust_id
// HAVING count(*) > 1

db.orders.aggregate( [
  {
    $group: {
      _id: "$cust_id",
      count: { $sum: 1 }
    }
  },
  { $match: { count: { $gt: 1 } } }
] );
