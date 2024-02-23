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


def list_states(username, password, database, element):
    """my Orm"""
    myturple = ();
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)
    cursor = db.cursor()

    # Execute SQL query to select states with the specified name
    cursor.execute("SELECT cities.id, cities.name, states.name\
                   FROM cities JOIN states ON cities.state_id = states.id \
                            WHERE states.name = %s ORDER BY cities.id ASC", (element,))

    # Fetch all rows
    cities = cursor.fetchall()

    # Display results
    for city in cities:
        new = city[1:]
        myturple += new
    
    for state in myturple:
        print(state, end=', ')


    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username>\
              <password> <database>")
        sys.exit(1)

    username, password, database, element = sys.argv[1:]

    list_states(username, password, database, element)

