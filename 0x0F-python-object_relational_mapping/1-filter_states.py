#!/usr/bin/python3
"""
This script lists  all states with the name starting with N from hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=db_name,
            port=3306)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    conn.close()
