db = db.getSiblingDB('myNewDB');

// SELECT COUNT(*)
// FROM (SELECT cust_id,
//              ord_date
//       FROM orders
//       GROUP BY cust_id,
//                ord_date)
//       as DerivedTable

db.orders.aggregate( [
  {
    $group: {
      _id: {
        cust_id: "$cust_id",
        ord_date: { $dateToString: {
          format: "%Y-%m-%d",
          date: "$ord_date"
        }}
      }
    }
  },
  {
    $group: {
      _id: null,
      count: { $sum: 1 }
    }
  }
] );
