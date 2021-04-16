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
    "WHERE salary >= %s "
)

print(sql)

min_salary_filter = 115000
cursor.execute(sql, (min_salary_filter, ))

for (f, l, s) in cursor:
    print(f, l, s, sep="/")
