#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro

import pymysql as mariadb
from decimal import Decimal


def create_connection(
        host='localhost',
        database='BenBrumm',
        user="myAdmin",
        password="myAdmin"):
    """ create a database connection to the MariaDB database
        specified by the params
    :param host: the hostname or IP
    :param database: name of the database
    :param user: username
    :param password: password
    :return: connection object or None
    """
    conn = None
    try:
        conn = mariadb.connect(
            host=host, database=database,
            user=user, password=password)
    except mariadb.Error as e:
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
    sql += " LIMIT %s"
    cur = conn.cursor()
    cur.execute(sql, (limit,))

    fields = map(lambda d: d[0], cur.description)
    print(list(fields))
    rows = cur.fetchall()
    for row in rows:
        # print(row)
        line = []
        for data in row:
            if type(data) is Decimal:
                line.append(float(data))
            else:
                line.append(str(data))
        print(line)


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
SELECT Country, COUNT(Country) AS cnt
  FROM Customer
  GROUP BY Country
  ORDER BY COUNT(Country) DESC
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
SELECT
  InvoiceId,
  Amount AS MaxInvoice
  FROM (
        SELECT
              InvoiceId,
              SUM(UnitPrice * Quantity) AS Amount
          FROM InvoiceLine
          GROUP BY  InvoiceId
        ) x
  ORDER BY Amount DESC
    """

    execute_sql(conn, sql, 1)


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
SELECT
      COUNT(il.Quantity) AS "Times_Purchased",
      t.Trackid,
      t.Name,
      m.Name AS "Media_Type",
      m.MediaTypeId
  FROM Track t
       JOIN MediaType    m ON m.MediaTypeId = t.MediaTypeId
       JOIN InvoiceLine il ON il.TrackId = t.Trackid
  GROUP BY m.Name
  ORDER BY "Times_Purchased" DESC
    """

    execute_sql(conn, sql)


if __name__ == '__main__':
    conn = create_connection(database="Chinook")
    print("1)", "~" * 50)
    exercise_01(conn)
    print("2)", "~" * 50)
    exercise_02(conn)
    print("3)", "~" * 50)
    exercise_03(conn)
