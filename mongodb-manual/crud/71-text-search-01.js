db = db.getSiblingDB('MyMongoManual');

db.stores.createIndex( { name: "text", description: "text" } );

db.stores.find( { $text: { $search: "java coffee shop" } } );

db.stores.find( { $text: { $search: "\"coffee shop\"" } } );

db.stores.find( { $text: { $search: '"coffee shop"' } } );

db.stores.find( { $text: { $search: "java shop -coffee" } } );

db.stores.find(
  { $text: { $search: "java coffee shop" } },
  { score: { $meta: "textScore" }
  }).sort( { score: { $meta: "textScore" } } );
