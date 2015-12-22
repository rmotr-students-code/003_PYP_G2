import sqlite3

db = sqlite3.connect('database.db')

cursor = db.execute('INSERT INTO author (country_id, name) VALUES (1, "Testing 123");');
print(cursor.fetchall())