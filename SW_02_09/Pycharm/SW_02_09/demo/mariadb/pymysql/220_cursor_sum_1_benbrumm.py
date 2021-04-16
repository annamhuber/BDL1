#!/usr/bin/env python3
# 2019-11, Bruno Grossniklaus, https://github.com/it-gro

import pymysql as mariadb

mariadb_connection = mariadb.connect(
    host='localhost', database='BenBrumm',
    user='myAdmin', password='myAdmin')
cursor = mariadb_connection.cursor()

print("1)", "~" * 50)
sql = (
    "SELECT first_name, last_name, salary "
    "FROM employee "
    "WHERE first_name LIKE %s "
    "  AND last_name LIKE %s "
)

print(sql)

first_name_filter = 'B%'
last_name_filter = 'G%'
cursor.execute(sql, (first_name_filter, last_name_filter))

for (f, l, s) in cursor:
    print(f, l, s, sep="/")

print("2)", "~" * 50)
cursor.execute(sql, (first_name_filter, last_name_filter))
total_salary = 0
for (f, l, s) in cursor:
    total_salary += s

print(total_salary)

print("3)", "~" * 50)
sql = (
    "SELECT SUM(salary) "
    "FROM employee "
    "WHERE first_name LIKE %s "
    "  AND last_name LIKE %s "
    #     "  AND 1=0 "
)

print(sql)

cursor.execute(sql, (first_name_filter, last_name_filter))
for (t,) in cursor:
    print(t)
