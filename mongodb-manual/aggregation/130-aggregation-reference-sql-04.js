db = db.getSiblingDB('myNewDB');

// SELECT cust_id, SUM(price) AS total FROM orders GROUP BY cust_id

db.orders.aggregate( [
  {
    $group: {
      _id: "$cust_id",
      total: { $sum: "$price" }
    }
  }
] );
