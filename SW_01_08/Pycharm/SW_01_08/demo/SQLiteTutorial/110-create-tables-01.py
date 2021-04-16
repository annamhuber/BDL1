#!/usr/bin/env python3
# 2020-03, Bruno Grossniklaus, https://github.com/it-gro
# https://www.sqlitetutorial.net/sqlite-python/create-tables/

import sqlite3
import pathlib

# import os
# os.chdir(Path.home())
base_dir = str(pathlib.Path.home()) + "/bdl03-1/sqlite"
db_file = f"{base_dir}/pythonsqlite.db"


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


def create_tables(database):
    sql_create_projects_table = """
CREATE TABLE IF NOT EXISTS projects (
id         INTEGER PRIMARY KEY,
name       TEXT    NOT NULL   ,
begin_date TEXT               ,
end_date   TEXT
);
"""

    sql_create_tasks_table = """
CREATE TABLE IF NOT EXISTS tasks (
id          INTEGER PRIMARY KEY,
name        TEXT    NOT NULL   ,
priority    INTEGER            ,
status_id   INTEGER NOT NULL   ,
project_id  INTEGER NOT NULL   ,
begin_date  TEXT    NOT NULL   ,
end_date    TEXT    NOT NULL   ,
FOREIGN KEY (project_id) REFERENCES projects (id)
);
"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    create_tables(db_file)
