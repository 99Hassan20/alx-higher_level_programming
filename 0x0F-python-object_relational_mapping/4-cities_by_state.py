#!/usr/bin/python3
"""script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where
name matches the argument. But this time, this one is
safe from MySQL injections"""
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
    query = "select city.id, city.name, state.name from\
        cities as city inner join states as state\
            on city.state_id=state.id order by city.id asc;"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
