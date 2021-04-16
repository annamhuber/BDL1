#!/usr/bin/env bash

cd $(dirname $0)
js="$(basename $0 .sh).js"
mongo --quiet "localhost:27017/mongodb-examples" < "${js}"
