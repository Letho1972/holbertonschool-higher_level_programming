#!/usr/bin/python3

"""Write a script that lists all cities from the database"""

import MySQLdb
import sys

if __name__ == "__main__":

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = database.cursor()

    cursor.execute("SELECT * FROM cities ORDER BY cities.id;")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    database.close()
