#!/usr/bin/python3
"""
This script lists all cities from database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

    conn = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=db_name,
            port=3306
            )

    cursor = conn.cursor()
    query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """
    cursor.execute(query, (state,))
    results = cursor.fetchall()

    if results:
        print(", ".join(city[0] for city in results))
    else:
        print("")

    cursor.close()
    conn.close()
