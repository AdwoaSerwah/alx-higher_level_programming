#!/usr/bin/python3
"""
This script takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    st = sys.argv[4]

    conn = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=db_name,
            port=3306
            )

    cursor = conn.cursor()
    query = (
            "SELECT * FROM states "
            "WHERE name = '{}' "
            "COLLATE utf8mb4_bin "
            "ORDER BY id ASC".format(st)
            )
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    conn.close()
