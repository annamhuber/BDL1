db = db.getSiblingDB('MyMongoManual');

cursor=db.categories_path.find().sort( { path: 1 } )
cursor.forEach(printjson)

cursor=db.categories_path.find( { path: /,Programming,/ } )
cursor.forEach(printjson)

cursor=db.categories_path.find( { path: /^,Books,/ } )
cursor.forEach(printjson)

db.categories_path.createIndex( { path: 1 } )
