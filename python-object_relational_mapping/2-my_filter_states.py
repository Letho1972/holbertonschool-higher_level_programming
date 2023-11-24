#!/usr/bin/python3

"""Write a script that takes in
an argument and displays all values in the states
where name matches the argument."""

import MySQLdb
import sys

if __name__ == "__main__":

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
    )
    cursor = database.cursor()

    cursor.execute("SELECT * FROM states WHERE name = '{}' \
                   ORDER BY id;".format(sys.argv[4]))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    database.close()
