#!/usr/bin/python3
"""A module to list all states from the hbtn_0e_0_usa database.

This module provides a function to connect to a MySQL database and retrieve
a list of all states from the hbtn_0e_0_usa database. The function takes
three arguments: username, password, and database name.

Example:
    $ python 0-select_states.py root root hbtn_0e_0_usa

Attributes:
    None
"""
import MySQLdb
import sys


def list_states(username, password, database):
    """my Orm"""
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)
    cursor = db.cursor()
    # Execute SQL query to select all states
    cursor.execute("SELECT * FROM states WHERE name\
                   LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch all rows
    states = cursor.fetchall()
    # Display results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:]
    list_states(username, password, database)