#!/usr/bin/env python3
# 2020-03, Bruno Grossniklaus, https://github.com/it-gro
# https://www.mysqltutorial.org/python-connecting-mysql-databases

import pymysql


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = pymysql.connect(
            host='localhost', database='python_mysql',
            user='myAdmin', password='myAdmin')

        if conn.open:
            print('Connected to MySQL database')

    except pymysql.Error as e:
        print(e)

    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    connect()
