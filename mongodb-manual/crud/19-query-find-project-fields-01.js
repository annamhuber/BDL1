db = db.getSiblingDB('MyMongoManual');

// SELECT * from inventory WHERE status = "A"
db.inventory.find( { status: "A" } )

// SELECT _id, item, status from inventory WHERE status = "A"
db.inventory.find( { status: "A" }, { item: 1, status: 1 } )

// SELECT item, status from inventory WHERE status = "A"
db.inventory.find( { status: "A" }, { item: 1, status: 1, _id: 0 } )

db.inventory.find( { status: "A" }, { status: 0, instock: 0 } )

db.inventory.find(
  { status: "A" },
  { item: 1, status: 1, "size.uom": 1 }
)

db.inventory.find(
  { status: "A" },
  { "size.uom": 0 }
)

db.inventory.find( { status: "A" },
                   { item: 1, status: 1, "instock.qty": 1 } )

db.inventory.find( { status: "A" },
                   { item: 1, status: 1, instock: { $slice: -1 } } )
