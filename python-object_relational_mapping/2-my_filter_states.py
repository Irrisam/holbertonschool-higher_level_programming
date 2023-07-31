#!bin/bash/python3
""" a script that takes in an argument and displays all values in the states"""
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
    search_value = sys.argv[4]
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE states.name
                LIKE BINARY %s ORDER BY states.id""", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
