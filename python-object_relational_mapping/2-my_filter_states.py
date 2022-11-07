#!/usr/bin/python3
"""
  Takes in an argument and displays all values in the states table of
  hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    # make a connection and 3 arguments take in
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()   # create a cursor
    # execute query
    cur.execute("SELECT * FROM states WHERE name='{:s}'\
    ORDER BY id ASC".format(argv[4]))
    # fetch and print
    rows = cur.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    # close all cursor and database
    cur.close()
    db.close()
