#!/usr/bin/python3
"""
  The filter states by the user input
  And save from SQL injection
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # make a connection and 3 arguments take in
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()   # create a cursor

    # execute query
    cur.execute("SELECT * FROM states WHERE name='{}'\
    ORDER BY id ASC".format(argv[4]))

    # fetch and print
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # close all cursor and database
    cur.close()
    db.close()
