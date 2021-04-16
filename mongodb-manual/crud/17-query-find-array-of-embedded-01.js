db = db.getSiblingDB('MyMongoManual');

db.inventory.find( { "instock": { warehouse: "A", qty: 5 } } );

db.inventory.find( { "instock": { qty: 5, warehouse: "A" } } );

db.inventory.find( { 'instock.qty': { $lte: 20 } } );

db.inventory.find( { 'instock.0.qty': { $lte: 20 } } );

db.inventory.find( { "instock":
                     { $elemMatch: { qty: 5, warehouse: "A" } } } );

db.inventory.find( { "instock":
                     { $elemMatch: { qty: { $gt: 10, $lte: 20 } } } } );

db.inventory.find( { "instock.qty": { $gt: 10,  $lte: 20 } } );

db.inventory.find( { "instock.qty": 5, "instock.warehouse": "A" } );
