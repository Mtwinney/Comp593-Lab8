import os
import sqlite3
import pandas as pd

# Determine the path of the database
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'music_library.db')

def main():
    # Create the database and its tables
    create_music_db()

    # Query DB for list of married couples
    married_couples = get_married_couples()

    # Save all married couples to CSV file
    csv_path = os.path.join(os.path.dirname(__file__), 'married_couples.csv')
    save_married_couples_csv(married_couples, csv_path)

def create_music_db():
    """Creates the music database and all of its tables"""
    # Open a connection to the database.
    con = sqlite3.connect(db_path)

    # Get a Cursor object that can be used to run SQL queries on the database.
    cur = con.cursor()

    # Define your SQL queries to create the necessary tables.
    create_album_table_query = """
        CREATE TABLE IF NOT EXISTS albums 
        (
            id      INTEGER PRIMARY KEY, 
            title   TEXT NOT NULL, 
            artist  TEXT NOT NULL, 
            year    INTEGER NOT NULL
        ); 
    """

    # Define other tables' creation queries here...

    # Execute the SQL queries to create the tables.
    cur.execute(create_album_table_query)

    # Commit the transaction and close the connection.
    con.commit()
    con.close()

def get_married_couples():
    """Queries the Social Network database for all married couples.

    Returns:
        list: (name1, name2, start_date) of married couples 
    """
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # SQL query to get married couples
    married_couples_query = """
    SELECT p1.name AS person1_name, p2.name AS person2_name, r.start_date
    FROM relationships AS r
    JOIN people AS p1 ON r.person1_id = p1.id
    JOIN people AS p2 ON r.person2_id = p2.id
    WHERE r.type = 'spouse'
    """
    cur.execute(married_couples_query)
    married_couples = cur.fetchall()
    con.close()
    return married_couples

def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """
    columns = ['Person 1', 'Person 2', 'Start Date']
    married_couples_df = pd.DataFrame(married_couples, columns=columns)
    married_couples_df.to_csv(csv_path, index=False)

if __name__ == '__main__':
    main()
