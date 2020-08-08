#!/usr/bin/python3
""" query all states from the db
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id ASC")
    for d in c.fetchall():
        print(d)
    c.close()
    db.close()
