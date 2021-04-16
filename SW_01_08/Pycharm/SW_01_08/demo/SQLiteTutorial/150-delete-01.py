#!/usr/bin/env python3
# 2020-03, Bruno Grossniklaus, https://github.com/it-gro
# https://www.sqlitetutorial.net/sqlite-python/delete/
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
    except sqlite3.Error as e:
        print(e)

    return conn


def delete_task(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_all_tasks(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM tasks'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def main():
    database = db_file

    # create a database connection
    conn = create_connection(database)
    with conn:
        delete_task(conn, 2)
        # delete_all_tasks(conn)


if __name__ == '__main__':
    main()
