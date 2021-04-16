db = db.getSiblingDB('mongodb-examples');

db.restaurants.find({}).limit(5)
db.restaurants.find({}).limit(5).pretty()

var cursor = db.restaurants.find({}).limit(5)
cursor.forEach(function(myDoc) { printjson(myDoc); } )

// :-/
var cursor = db.restaurants.find({}).limit(5)
cursor.toArray().slice(0,3).forEach(function(myDoc) { printjson(myDoc); } )
