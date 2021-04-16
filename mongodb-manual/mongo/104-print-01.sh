#!/usr/bin/env bash

myDB="localhost:27017/mongodb-examples"
myCollection="restaurants"

cat <<EOF | mongo --quiet "${myDB}"
  db.restaurants.find({}).limit(2);

  // :-/
  db.${myCollection}.find({}).limit(2).pretty();

  // :-)
  db['${myCollection}'].find({}).limit(2)
EOF
