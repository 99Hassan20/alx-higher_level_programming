#!/usr/bin/python3
""" lists all states with a name
    starting with N (upper N) from the database hbtn_0e_0_usa"""
from sys import argv, exit
import MySQLdb as mysql

if __name__ == "__main__":
    if (len(argv)) != 4:
        print(f"Usage: python3 {__file__} username password database")
        exit(0)
    _user = argv[1]
    _passwd = argv[2]
    dbname = argv[3]
    _host = "localhost"

    db = mysql.connect(host=_host, user=_user,
                       passwd=_passwd, db=dbname, port=3306)
    cur = db.cursor()
    cur.execute("select * from states where\
                name like binary 'N%' order by states.id asc")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
