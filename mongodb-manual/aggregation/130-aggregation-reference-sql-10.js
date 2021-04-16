db = db.getSiblingDB('myNewDB');

// SELECT cust_id,
//        SUM(price) as total
// FROM orders
// WHERE status = 'A'
// GROUP BY cust_id
// HAVING total > 50

db.orders.aggregate( [
  { $match: { status: 'A' } },
  {
    $group: {
      _id: "$cust_id",
      total: { $sum: "$price" }
    }
  },
  { $match: { total: { $gt: 50 } } }
] );
