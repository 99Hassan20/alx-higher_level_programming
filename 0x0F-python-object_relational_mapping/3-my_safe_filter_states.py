#!/usr/bin/python3
"""script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where
name matches the argument. But this time, this one is
safe from MySQL injections"""
from sys import argv, exit
import MySQLdb as mysql

if __name__ == "__main__":
    if (len(argv)) != 5:
        print(f"Usage: python3 {__file__} username password database city")
        exit(0)
    _user = argv[1]
    _passwd = argv[2]
    dbname = argv[3]
    _host = "localhost"
    name = argv[4]

    db = mysql.connect(host=_host, user=_user,
                       passwd=_passwd, db=dbname, port=3306)
    cur = db.cursor()
    query = "select * from states where\
                name like binary %s order by states.id asc"
    cur.execute(query, (name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
