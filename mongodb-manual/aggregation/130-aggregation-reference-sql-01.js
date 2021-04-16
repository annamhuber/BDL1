db = db.getSiblingDB('myNewDB');

db.orders.deleteMany({});

db.orders.insertMany(
  [
    {
      cust_id: "abc123",
      ord_date: ISODate("2012-11-02T17:04:11.102Z"),
      status: 'A',
      price: 50,
      items: [ { sku: "xxx", qty: 25, price: 1 },
               { sku: "yyy", qty: 25, price: 1 } ]
    }
    ,{
      cust_id: "def456",
      ord_date: ISODate("2012-11-02T18:00:00.102Z"),
      status: 'A',
      price: 60,
      items: [ { sku: "xxx", qty: 40, price: 1 },
               { sku: "yyy", qty: 10, price: 1 },
               { sku: "zzz", qty: 10, price: 1 } ]
    }
    ,{
      cust_id: "abc123",
      ord_date: ISODate("2012-12-15T18:00:00.102Z"),
      status: 'A',
      price: 70,
      items: [ { sku: "yyy", qty: 70, price: 1 } ]
    }
  ]
);
