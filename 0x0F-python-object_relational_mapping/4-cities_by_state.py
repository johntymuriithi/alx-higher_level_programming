#!/usr/bin/python3
"""A script to list all cities from the database hbtn_0e_4_usa."""

import MySQLdb
import sys

def list_cities(username, password, database):
    """Connect to the MySQL server and list all cities."""
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database)
        cursor = db.cursor()

        # Execute SQL query to select all cities
        cursor.execute("SELECT * FROM cities ORDER BY id ASC")

        # Fetch all rows
        cities = cursor.fetchall()

        # Display results
        for city in cities:
            print(city)

    except MySQLdb.Error as e:
        print("Error accessing database:", e)

    finally:
        # Close cursor and database connection
        if 'db' in locals() and db is not None:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:]

    list_cities(username, password, database)

