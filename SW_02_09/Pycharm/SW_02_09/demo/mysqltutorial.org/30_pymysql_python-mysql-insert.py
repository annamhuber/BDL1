#!/usr/bin/env python3
# 2020-03, Bruno Grossniklaus, https://github.com/it-gro
# https://www.mysqltutorial.org/python-mysql-insert

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


def insert_book(conn, title, isbn):
    query = "INSERT INTO books(title,isbn) VALUES(%s,%s)"
    args = (title, isbn)

    try:
        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()

    except pymysql.Error as e:
        print(e)

    finally:
        cursor.close()


def insert_books(conn, books):
    query = "INSERT INTO books(title,isbn) VALUES(%s,%s)"

    try:
        cursor = conn.cursor()
        cursor.executemany(query, books)

        conn.commit()

    except pymysql.Error as e:
        print(e)

    finally:
        cursor.close()


def main():
    conn = connect()
    insert_book(conn, 'A Sudden Light', '9781439187036')

    books = [
        ('Harry Potter And The Order Of The Phoenix', '9780439358071'),
        ('Gone with the Wind', '9780446675536'),
        ('Pride and Prejudice (Modern Library Classics)', '9780679783268')
    ]
    insert_books(conn, books)
    conn.close()


if __name__ == '__main__':
    main()
