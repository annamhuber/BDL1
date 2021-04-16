db = db.getSiblingDB('myNewDB');

// SELECT SUM(price) AS total FROM orders

db.orders.aggregate( [
  {
    $group: {
      _id: null,
      total: { $sum: "$price" }
    }
  }
] );
