db = db.getSiblingDB('myNewDB');

// SELECT COUNT(*) AS count FROM orders

db.orders.aggregate( [
  {
    $group: {
      _id: null,
      count: { $sum: 1 }
    }
  }
] );
