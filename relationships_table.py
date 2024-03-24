import sqlite3
con = sqlite3.connect('social_network.db')
cur = con.cursor()
# SQL query that creates a table named 'relationships'.
create_relationships_tbl_query = """
    CREATE TABLE IF NOT EXISTS relationships
    (
        id INTEGER PRIMARY KEY,
        person1_id INTEGER NOT NULL,
        person2_id INTEGER NOT NULL,
        type TEXT NOT NULL,
        start_date DATE NOT NULL,
        FOREIGN KEY (person1_id) REFERENCES people (id),
        FOREIGN KEY (person2_id) REFERENCES people (id)
    );
"""
# Execute the SQL query to create the 'relationships' table.
cur.execute(create_relationships_tbl_query)
con.commit()
con.close()