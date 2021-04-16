db = db.getSiblingDB('MyMongoManual');

db.places.insert( {
  name: "Central Park",
  location: { type: "Point", coordinates: [ -73.97, 40.77 ] },
  category: "Parks"
});

db.places.insert( {
  name: "Sara D. Roosevelt Park",
  location: { type: "Point", coordinates: [ -73.9928, 40.7193 ] },
  category: "Parks"
});

db.places.insert( {
  name: "Polo Grounds",
  location: { type: "Point", coordinates: [ -73.9375, 40.8303 ] },
  category: "Stadiums"
});

db.places.createIndex( { location: "2dsphere" } );

db.places.find();

db.places.find(
  {
    location:
    { $near:
      {
        $geometry: { type: "Point",  coordinates: [ -73.9667, 40.78 ] },
        $minDistance: 1000,
        $maxDistance: 5000
      }
    }
  }
);

db.places.aggregate( [
  {
    $geoNear: {
      near: { type: "Point", coordinates: [ -73.9667, 40.78 ] },
      spherical: true,
      query: { category: "Parks" },
      distanceField: "calcDistance"
    }
  }
]);
