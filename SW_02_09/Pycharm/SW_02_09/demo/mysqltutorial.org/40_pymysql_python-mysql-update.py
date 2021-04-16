#!/usr/bin/env python3
# 2020-03, Bruno Grossniklaus, https://github.com/it-gro
# https://www.mysqltutorial.org/python-mysql-update

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


def update_book(conn, book_id, title):
    # prepare query and data
    query = """ UPDATE books
                SET title = %s
                WHERE id = %s """

    data = (title, book_id)

    try:
        # update book title
        cursor = conn.cursor()
        cursor.execute(query, data)

        # accept the changes
        conn.commit()

    except pymysql.Error as e:
        print(e)

    finally:
        cursor.close()


def main():
    conn = connect()
    update_book(conn, 37, 'The Giant on the Hill *** TEST ***')
    conn.close()


if __name__ == '__main__':
    main()
