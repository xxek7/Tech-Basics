import sqlite3

#connect to database
conn = sqlite3.connect('users.db')

#create a cursor
c = conn.cursor()

#create a table
c.execute("""CREATE TABLE users (
	first_name text,
	last_name text,
	email text)

	""")

conn.commit()
