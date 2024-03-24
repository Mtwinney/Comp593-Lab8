import sqlite3
from random import randint, choice
from faker import Faker
con = sqlite3.connect('social_network.db')
cur = con.cursor()
# SQL query that inserts a row of data in the relationships table.
add_relationship_query = """
INSERT INTO relationships
(
person1_id,
person2_id,
type,
start_date
)
VALUES (?, ?, ?, ?);
"""
fake = Faker()
# Randomly select first person in relationship
person1_id = randint(1, 200)
# Randomly select second person in relationship
# Loop ensures person will not be in a relationship with themself
person2_id = randint(1, 200)
while person2_id == person1_id:
    person2_id = randint(1, 200)
# Randomly select a relationship type
rel_type = choice(('friend', 'spouse', 'partner', 'relative'))
# Randomly select a relationship start date between now and 50 years ago
start_date = fake.date_between(start_date='-50y', end_date='today')
# Create tuple of data for the new relationship
new_relationship = (person1_id, person2_id, rel_type, start_date)
# Add the new relationship to the DB
cur.execute(add_relationship_query, new_relationship)
con.commit()
con.close()