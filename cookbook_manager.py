#use SQLite database

import sqlite3
from sqlite3 import Error

#Function to create a connection to the database
def create_connection():
    """Create a database connection"""
    conn = None
    try:
        conn = sqlite3.connect('hipster_cookbooks.db')
        #print if it worked
        print(f"Successfully connected to SQLite {sqlite3.version}")
        return conn
    except Error as e:
        #print if it didn't work
        print(f"Error establishing connection with the void: {e}")
        return None
    
#Function to create a table for storing cookbooks
def create_table(conn):
    """Create table structure"""
    try: 
        sql_create_cookbooks_table = """
        CREATE TABLE IF NOT EXISTS cookbooks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEX NOT NULL,
        year_published INTEGER,
        aesthetic_rating INTEGER,
        instagram_worthy BOOLEAN,
        cover_color TEXT
    );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_cookbooks_table)
        print("Sucessfully createdd a database structure")
    except Error as e:
        print(f"Error creating a table: {e}")