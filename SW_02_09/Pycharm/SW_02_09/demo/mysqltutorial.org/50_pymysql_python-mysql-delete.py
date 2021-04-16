#!/usr/bin/env python3
# 2020-03, Bruno Grossniklaus, https://github.com/it-gro
# https://www.mysqltutorial.org/python-mysql-delete

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


def delete_book(conn, book_id):
    query = "DELETE FROM books WHERE id = %s"

    try:
        # execute the query
        cursor = conn.cursor()
        cursor.execute(query, (book_id,))

        # accept the change
        conn.commit()

    except pymysql.Error as e:
        print(e)

    finally:
        cursor.close()


def main():
    conn = connect()
    delete_book(conn, 102)
    conn.close()


if __name__ == '__main__':
    main()
