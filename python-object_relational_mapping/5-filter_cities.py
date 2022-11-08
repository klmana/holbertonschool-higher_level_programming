#!/usr/bin/python3
"""
  Script that takes in the name of a state as an argument
  and lists all cities of that state, using the database hbtn_0e_4_usa
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
    cur.execute("SELECT cities.name FROM cities \
    INNER JOIN states ON cities.state_id=states.id \
    WHERE states.name = %s ORDER BY cities.id", (argv[4],))

    # fetch and print
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))

    # close all cursor and database
    cur.close()
    db.close()
