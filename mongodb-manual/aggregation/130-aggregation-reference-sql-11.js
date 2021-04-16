db = db.getSiblingDB('myNewDB');

// SELECT cust_id,
//        SUM(li.qty) as qty
// FROM orders o,
//      order_lineitem li
// WHERE li.order_id = o.id
// GROUP BY cust_id

db.orders.aggregate( [
  { $unwind: "$items" },
  {
    $group: {
      _id: "$cust_id",
      qty: { $sum: "$items.qty" }
    }
  }
] );
