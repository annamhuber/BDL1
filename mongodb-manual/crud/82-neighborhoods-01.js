db = db.getSiblingDB('mongodb-examples');

db.restaurants.findOne();

db.neighborhoods.findOne(
  {
    geometry:
    { $geoIntersects:
      { $geometry:
        { type: "Point",
          coordinates: [ -73.93414657, 40.82302903 ]
        }
      }
    }
  }
);

var neighborhood = db.neighborhoods.findOne(
  { geometry:
    { $geoIntersects:
      { $geometry:
        { type: "Point",
          coordinates: [ -73.93414657, 40.82302903 ]
        }
      }
    }
  }
);

db.restaurants.find(
  { location:
    { $geoWithin:
      { $geometry: neighborhood.geometry }
    }
  }
).count();

db.restaurants.find(
  { location:
    { $geoWithin:
      { $centerSphere:
        [ [ -73.93414657, 40.82302903 ], 5 / 3963.2 ]
      }
    }
  }
);

db.restaurants.find(
  { location:
    { $nearSphere:
      { $geometry:
        { type: "Point",
          coordinates: [ -73.93414657, 40.82302903 ] },
        $maxDistance: 5 * 1609.34
      }
    }
  }
);
