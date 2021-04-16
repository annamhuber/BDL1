db = db.getSiblingDB('MyMongoManual');

db.inventory.find( { tags: ["red", "blank"] } );

db.inventory.find( { tags: { $all: ["red", "blank"] } } );

db.inventory.find( { tags: "red" } );

db.inventory.find( { dim_cm: { $gt: 25 } } );

db.inventory.find( { dim_cm: { $gt: 15, $lt: 20 } } );

db.inventory.find( { dim_cm: { $elemMatch: { $gt: 22, $lt: 30 } } } );

db.inventory.find( { "dim_cm.1": { $gt: 25 } } );

db.inventory.find( { "tags": { $size: 3 } } );
