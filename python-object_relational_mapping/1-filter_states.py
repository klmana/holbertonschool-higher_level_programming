#!/usr/bin/python3
"""
 Lists all states with a name starting with N
 (upper N) from the database hbtn_0e_0_usa:
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    # make a connection and 3 arguments take in
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()  # create a cursor
    # execute query
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' \
ORDER BY id ASC")
    # Fetch and print
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Close all cursor and database
    cur.close()
    db.close()
