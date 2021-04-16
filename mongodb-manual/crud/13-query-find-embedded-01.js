db = db.getSiblingDB('MyMongoManual');

db.inventory.find( { size: { h: 14, w: 21, uom: "cm" } } );
db.inventory.find( { size: { w: 21, h: 14, uom: "cm" } } );

db.inventory.find( { "size.uom": "in" } );
db.inventory.find( { "size.h": { $lt: 15 } } );
db.inventory.find( { "size.h": { $lt: 15 },
                     "size.uom": "in", status: "D" } );
