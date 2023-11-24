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

    cursor.execute("SELECT cities.name FROM states \
                JOIN cities ON states.id = cities.state_id \
                WHERE states.name = %s \
                ORDER BY cities.id;", (sys.argv[4],))

    rows = cursor.fetchall()

    city_names = ', '.join(row[0] for row in rows)

    print(city_names)

    cursor.close()
    database.close()
