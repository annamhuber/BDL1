#!/usr/bin/env python3
# 2019-11, Bruno Grossniklaus, https://github.com/it-gro

import mysql.connector as mariadb

mariadb_connection = mariadb.connect(
    host='localhost', database='employees',
    user='myAdmin', password='myAdmin')
cursor = mariadb_connection.cursor()

sql = """
SELECT first_name, last_name
FROM employees
WHERE first_name LIKE %s
"""

print(sql)

print("1)", "~" * 50)

first_name_filter = 'Bab%'
cursor.execute(sql, (first_name_filter, ))

for row in cursor:
    print(row)


print("2)", "~" * 50)

first_name_filter = 'Can%'
cursor.execute(sql, (first_name_filter, ))

for (f, l) in cursor:
    print(f, l, sep="/")
