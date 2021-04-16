#!/usr/bin/env bash

myDB="localhost:27017/mongodb-examples"
myCollection="primer-dataset"

cat <<'EOF' | mongo --quiet "${myDB}"
  db['primer-dataset'].find({}).limit(2).pretty()

  db['primer-dataset'].aggregate([
    {$limit: 5},
    {$project: {borough: 1, cuisine: 1, _id: 0}},
  ])

EOF
