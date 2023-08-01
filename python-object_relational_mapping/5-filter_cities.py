#!/usr/bin/python3
"""a script that takes in the name of a state as an argument and lists all
cities of that state"""

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
    cur = db.cursor()
    query = """
            SELECT cities.name FROM cities JOIN states ON cities.state_id =
            states.id WHERE states.name = %s
            """
    cur.execute(query, (sys.argv[4],))

    rows = cur.fetchall()
    name = []
    for row in rows:
        name.append(row[0])
    output = ", ".join(name)
    print(output)

    cur.close()
    db.close()
