db = db.getSiblingDB('MyMongoManual');

c = db.categories_child.findOne( { _id: "Databases" } ).children
print(c)

db.categories_child.createIndex( { children: 1 } )

cursor = db.categories_child.find( { children: "MongoDB" } )
cursor.forEach(printjson)
