db = db.getSiblingDB('MyMongoManual');

db.inventory.find( { item: null } );
db.inventory.find( { item : { $type: 10 } } );
db.inventory.find( { item : { $exists: false } } );
