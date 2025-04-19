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
    
#Function to create tables for storing cookbooks and borrowing history
def create_tables(conn):
    """Create table structure"""
    try: 
        sql_create_cookbooks_table = """
        CREATE TABLE IF NOT EXISTS cookbooks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year_published INTEGER,
            aesthetic_rating INTEGER,
            instagram_worthy BOOLEAN,
            cover_color TEXT
        );"""
        
        """Create a borrowing history table"""
        sql_create_lending_cookbooks_table = """
        CREATE TABLE IF NOT EXISTS lending_cookbooks_list (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cookbook_id INTEGER NOT NULL, 
            borrower_name TEXT NOT NULL,
            date_borrowed DATE NOT NULL,
            returned BOOLEAN DEFAULT 0,
            date_returned DATE DEFAULT NULL,
            FOREIGN KEY (cookbook_id) REFERENCES cookbooks (id)
        );"""
        
        #To execute the above code: 
        #calling the constructor for the cursor object to create a new cursor
        #(let's us work with the database)
        cursor = conn.cursor()
        cursor.execute(sql_create_cookbooks_table)
        cursor.execute(sql_create_lending_cookbooks_table)
        print("Successfully created tables.")
    except Error as e:
        print(f"Error creating tables: {e}")
    
# part 2a
    # '''Function to create a new cookbook record'''

# Insert a new cookbook record into the database table:
def insert_cookbook(conn, cookbook):
    """Add a new cookbook to your shelf """
    sql = '''INSERT INTO cookbooks(title, author, year_published, 
        aesthetic_rating, instagram_worthy, cover_color)
        VALUES(?,?,?,?,?,?)'''
    
    #use the connection to the database to insert the new record:
    try: 
        #create a new cursor (like a pointer that lets us go through the database)
        cursor = conn.cursor()
        cursor.execute(sql, cookbook)
        #because we changed the database, need to commit the changes
        conn.commit()
        #print message if it worked:
        print(f"Successfully curated cookbook with id: {cursor.lastrowid}")
        return cursor.lastrowid
    except Error as e:
        #{e} contains stack trace for the error
        print(f"Error adding to collection: {e}")
        return None
    
#Function to retrieve the cookbooks from the database
def get_all_cookbooks(conn):
    """Browse your entire collection of cookbooks"""
    try: 
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cookbooks")
        #declare new variable (books), use the cursor to fetchall to 
        # return entire result set from our select statement into "books"
        books = cursor.fetchall()

        #Iterate through the list of books:
        for book in books:
            print(f"ID: {book[0]}")
            print(f"Title: {book[1]}")
            print(f"Author: {book[2]}")
            print(f"Published: {book[3]} (notes can be put here)")
            #multiply the emoji by the aesthetic rating: 
            print(f"Aesthetic Rating: {'*' * book[4]}")
            #insert some logic 
            print(f"Instagram Worthy: {'📸 Yes' if book[5] else 'Not aesthetic enough'}")
            print(f"Cover Color: {book[6]}")
            #this will separate info between books: 
            print("---")
        return books 
    except Error as e:
        print(f"Error retrieving collection: {e}")
        #returns an empty list:
        return []   

#TODO this is where to add new features:    
#part 2 new features to implement (do at least 2 features)
#option a, recipe tagging system:
def add_recipe_tags(conn, cookbook_id, tags):
    """Add tags to a cookbook (e.g., 'gluten-free', 'plant-based', 'artisanal')"""
    # Create a new tags table with many-to-many relationship
    # Implement tag addition functionality
    # Return success/failure status

#part 2, option b, cookbook borrowing tracker:
#made a table above first, then: 
def track_borrowed_cookbook(conn, cookbook_id, friend_name, date_borrowed):
    """Track which friend borrowed your cookbook and when"""

    # Part 2: Add new columns for tracking borrowed cookbooks

    # To execute the above code:
    # calling the constructor for the cursor object to create a new cursor
    # (let's us work with the database)
    cursor = conn.cursor()
    cursor.execute(sql_create_cookbooks_table)
    print("Successfully created a database structure")
        

    # Create a borrowing history table
    # Add borrowing record
    # Include return date tracking

#part 2, option c, Aesthetic Photoshoot Planning
# def create_photoshoot_plan(conn, cookbook_id):
#     """Generate Instagram-worthy photo layout suggestions based on cover_color and aesthetic_rating"""
    # Suggest photo angles
    # Recommend props based on cookbook theme
    # Generate hashtag suggestions

#part 2, option d, Seasonal Collection Rotation
# def rotate_seasonal_collection(conn, season):
#     """Update display recommendations based on season"""
    # Categorize books by season
    # Suggest seasonal arrangements
    # Update instagram_worthy status based on current season

#part 2, option e, Cookbook Analytics   
# def generate_collection_analytics(conn):
#     """Generate insights about your cookbook collection"""
    # Calculate average aesthetic rating
    # Track aesthetic trends by year
    # Identify gaps in your collection 


#main function is called with the program executes: (director)    
def main():
    #Establish connection to our cookbook database
    conn = create_connection()

    #Test if the connection is viable:
    if conn is not None:

        #drop table if exists:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS cookbooks")
        conn.commit()

        #Create our Table:
        create_tables(conn)

        # Insert some carefully curated sample cookbooks
        #main list: [], list into list ()
        cookbooks = [
            ('Foraged & Found: Mushrooms in Minnesota', 
             'Oak Wavelength', 2023, 5, True, 'Forest Green'),
            ('Small Batch: 50 Recipes for Cooking Solo', 
             'Sage Moonbeam', 2022, 4, True, 'Raw Linen'),
            ('The Artistic Toast: Advanced Avocado Techniques', 
             'River Wildflower', 2023, 5, True, 'Recycled Brown'),
            ('Fermented Everything', 
             'Jim Kombucha', 2021, 3, True, 'Denim'),
            ('The Deconstructed Sandwich', 
             'Juniper Vinegar-Smith', 2023, 5, True, 'Beige')
        ]
        
        #display our list of cookbooks:
        print("\nCurating your cookbook collection...")
        #first insert cookbooks into the database
        # loop through list of cookbooks
        for cookbook in cookbooks:
            insert_cookbook(conn, cookbook)
        
        #get the cookbooks from your database:
        print("\nYour carefully curated collection:")
        get_all_cookbooks(conn)
        
        #close the database connection
        conn.close()
        print("\nDatabase connection closed")
    else:
        print("Error! The universe is not aligned for database connections right now.")

if __name__ == '__main__':
    main()
