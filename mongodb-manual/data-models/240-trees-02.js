db = db.getSiblingDB('MyMongoManual');

var databaseCategory = db.categories_sets.findOne(
  { _id: "Databases" } );

cursor=db.categories_sets.find(
  {   left: { $gt: databaseCategory.left },
      right: { $lt: databaseCategory.right }
  } );
cursor.forEach(printjson)
