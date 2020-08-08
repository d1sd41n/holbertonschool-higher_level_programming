#!/usr/bin/python3
""" query all states from the db that starts with N
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT cities.name FROM cities JOIN states \
                ON cities.state_id=states.id WHERE states.name=%s \
                ORDER BY cities.id ASC", (sys.argv[4],))
    out = c.fetchall()
    cities = ", ".join([x[0] for x in out])
    print(cities)
    c.close()
    db.close()
