#!/usr/bin/python3
"""A script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument but safe from injections
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    # Use parameterized query with placeholder (%s)
    query = """
    SELECT *
    FROM states
    WHERE states.name LIKE BINARY %s
    ORDER BY states.id
    """
    # Pass the argument as a tuple to execute()
    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
