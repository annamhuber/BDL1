#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro

# migrate to pymysql (mariadb)
# localhost/Chinook (myAdmin/myAdmin)

import sqlite3
import pathlib

base_dir = str(pathlib.Path.home()) + "/bdl03-1/sqlite"
db_file = f"{base_dir}/Chinook.db"


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn


def execute_sql(conn, sql, limit=1000):
    """
    execute sql
    :param conn: the connection object
    :param sql: the sql statement
    :param limit: limit output
    :return:
    """
    sql += " LIMIT ?"
    cur = conn.cursor()
    cur.execute(sql, (limit,))

    rows = cur.fetchall()
    for row in rows:
        print(row)


def exercise_01(conn):
    """
    Top 5 countries of customers

    Country|cnt|
    -------|---|
    USA    | 13|
    Canada |  8|
    France |  5|
    Brazil |  5|
    Germany|  4|

    :param conn: the connection object
    :return:
    """

    sql = """
SELECT "ToDo"
    """

    execute_sql(conn, sql, 5)


def exercise_02(conn):
    """
    Highest invoice (with InvoiceId)?

    InvoiceId|MaxInvoice        |
    ---------|------------------|
          404|25.859999999999992|

    :param conn: the connection object
    :return:
    """

    sql = """
SELECT "ToDo"
    """

    execute_sql(conn, sql)


def exercise_03(conn):
    """
    Most sold media types

    Times_Purchased|TrackId|Name     ..|Media_Type    ..|MediaTypeId|
    ---------------|-------|---------..|--------------..|-----------|
               1976|      6|Put The F..|MPEG audio fil..|          1|
                146|      2|Balls to ..|Protected AAC ..|          2|
                111|   2820|Occupatio..|Protected MPEG..|          3|
                  4|   3479|Prometheu..|Purchased AAC ..|          4|
                  3|   3356|Muita Bob..|AAC audio file..|          5|

    :param conn: the connection object
    :return:
    """

    sql = """
SELECT "ToDo"
    """

    execute_sql(conn, sql)


if __name__ == '__main__':
    conn = create_connection(db_file)
    print("1)", "~" * 50)
    exercise_01(conn)
    print("2)", "~" * 50)
    exercise_02(conn)
    print("3)", "~" * 50)
    exercise_03(conn)
