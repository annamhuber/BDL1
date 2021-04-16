db = db.getSiblingDB('MyMongoManual');

a = db.categories_ancestors.findOne( { _id: "MongoDB" } ).ancestors
print(a)

db.categories_ancestors.createIndex( { ancestors: 1 } )

cursor = db.categories_ancestors.find( { ancestors: "Programming" } )
cursor.forEach(printjson)
