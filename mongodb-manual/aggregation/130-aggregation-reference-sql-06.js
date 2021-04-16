db = db.getSiblingDB('myNewDB');

// SELECT cust_id,
//        ord_date,
//        SUM(price) AS total
// FROM orders
// GROUP BY cust_id,
//          ord_date

db.orders.aggregate( [
  {
    $group: {
      _id: {
        cust_id: "$cust_id",
        ord_date: { $dateToString: {
          format: "%Y-%m-%d",
          date: "$ord_date"
        }}
      },
      total: { $sum: "$price" }
    }
  }
] );
