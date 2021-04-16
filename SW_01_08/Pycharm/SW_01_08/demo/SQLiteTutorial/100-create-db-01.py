#!/usr/bin/env python3
# 2020-03, Bruno Grossniklaus, https://github.com/it-gro
# https://www.sqlitetutorial.net/sqlite-python/creating-database/

import sqlite3
import pathlib

# import os
# os.chdir(Path.home())
base_dir = str(pathlib.Path.home()) + "/bdl03-1/sqlite"
db_file = f"{base_dir}/pythonsqlite.db"


def create_directory(dir):
    """ create path if not exists """
    if not pathlib.Path(dir).exists():
        pathlib.Path(dir).mkdir(parents=True)


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_directory(base_dir)
    create_connection(db_file)
