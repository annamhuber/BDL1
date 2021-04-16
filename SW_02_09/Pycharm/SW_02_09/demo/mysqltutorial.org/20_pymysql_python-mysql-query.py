#!/usr/bin/env python3
# 2020-03, Bruno Grossniklaus, https://github.com/it-gro
# https://www.mysqltutorial.org/python-mysql-query

import pymysql


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = pymysql.connect(
            host='localhost', database='python_mysql',
            user='myAdmin', password='myAdmin')

    except pymysql.Error as e:
        print(e)
        raise(e)

    return conn


def query_with_fetchone(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")

        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()

    except pymysql.Error as e:
        print(e)

    finally:
        cursor.close()


def query_with_fetchall(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()

        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)

    except pymysql.Error as e:
        print(e)

    finally:
        cursor.close()


def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


def query_with_fetchmany(conn):
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books")

        for row in iter_row(cursor, 10):
            print(row)

    except pymysql.Error as e:
        print(e)

    finally:
        cursor.close()


if __name__ == '__main__':
    conn = connect()
    query_with_fetchone(conn)
    print("1)", "~" * 50)
    query_with_fetchall(conn)
    print("2)", "~" * 50)
    query_with_fetchmany(conn)
    conn.close()
