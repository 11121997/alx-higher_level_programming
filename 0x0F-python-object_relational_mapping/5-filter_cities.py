#!/usr/bin/python3
"""script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""


if __name__ = "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.excute("""SELECT cities.name FROM cities
               LEFT JOIN states ON states.id = cities.state_id
               where states.name = %s
               ORDER BY cities.id ASC""", (sys.argv[4],))

    rows = cur.fetchall()
    length = len(rows)
    for i in range(length):
        if i < length - 1:
            print(rows[i][0], end=", ")
        else:
            print(rows[i][0])
