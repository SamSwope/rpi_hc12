import sqlite3

# This file holds helper functions for SQLite3 in Python
# It specifically is used for converting transmitted data
# to be inserted in a database

# This function creates a .db file with name x
# x must include .db in name
# The layout of the values in the database follow as:
# date TEXT, time TEXT, d1 REAL, d2 REAL, d3 REAL, d4 REAL, d5 REAL
def createdb(x):
    
    # Create file
    f = open(x)
    f.close()

    # Connect to SQL Database
    con = sqlite3.connect(x)
    c = con.cursor()

    # Create table for data
    c.execute("CREATE TABLE data (date TEXT, time TEXT, d1 REAL, d2 REAL, d3 REAL, d4 REAL, d5 REAL);")

    # Close database
    con.commit()
    con.close()