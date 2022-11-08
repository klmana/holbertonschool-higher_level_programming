#!/usr/bin/python3
"""
  Lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # make a connection and 3 arguments take in
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    # create a cursor
    cur = db.cursor()

    # execute query
    cur.execute("SELECT cities.id, cities.name, states.name \
    FROM cities INNER JOIN states ON cities.state_id = states.id \
    ORDER BY cities.id")

    # fetch and print
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # close all cursor and database
    cur.close()
    db.close()
