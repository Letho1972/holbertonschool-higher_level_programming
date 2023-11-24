#!/usr/bin/python3

"""Write a script that lists all states with a name starting with N"""

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

    # Execute the query to retrieve states starting with 'N'
    query = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id;"
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    cursor.close()
    database.close()
