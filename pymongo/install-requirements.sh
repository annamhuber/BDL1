#!/usr/bin/env bash
# 2019-08, Bruno Grossniklaus, https://github.com/it-gro

if [ -z "$VIRTUAL_ENV" ]; then
  echo "we are not in a virtual environment, exiting ..." >&2
  exit 1
fi

cd $(dirname $0)
pip3 install --upgrade --upgrade-strategy only-if-needed -r requirements.txt
