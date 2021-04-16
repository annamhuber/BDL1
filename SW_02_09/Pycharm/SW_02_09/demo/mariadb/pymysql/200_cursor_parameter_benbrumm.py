#!/usr/bin/env python3
# 2019-11, Bruno Grossniklaus, https://github.com/it-gro

import pymysql as mariadb

mariadb_connection = mariadb.connect(
    host='localhost', database='BenBrumm',
    user='myAdmin', password='myAdmin')
cursor = mariadb_connection.cursor()

print("1)", "~" * 50)
sql = (
    "SELECT first_name, last_name "
    "FROM employee "
    "WHERE first_name LIKE %s "
    "  AND last_name LIKE %s "
)

print(sql)

first_name_filter = 'B%'
last_name_filter = 'G%'
cursor.execute(sql, (first_name_filter, last_name_filter))

for row in cursor:
    print(row)
