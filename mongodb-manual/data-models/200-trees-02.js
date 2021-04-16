db = db.getSiblingDB('MyMongoManual');

p = db.categories_parent.findOne( { _id: "MongoDB" } ).parent
print(p)

db.categories_parent.createIndex( { parent: 1 } )

cursor = db.categories_parent.find( { parent: "Databases" } )
cursor.forEach(printjson)
