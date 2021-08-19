import sqlite3
from sqlite3.dbapi2 import connect

conn = sqlite3.connect('users_2.db')

c = conn.cursor()

c.execute("""CREATE TABLE users (
    first_name text,
    last_name text,
    username text,
    password text
    )
""")

conn.commit()

firstname = input("please enter your first name")
lastname = input("please enter your last name")
username = input("please choose a username")
password = input("please choose a password")

user = [ (firstname, lastname, username, password) ]

c.executemany("INSERT INTO users VALUES (?,?,?,?)", user)

conn.commit()


print ("Welcome to velocity!")

c.execute("SELECT * FROM users")

items = c.fetchall()

for item in items:
    print(item[0] + " " + item[1] + "\t" + item[2] + "\t" + item[3])

conn.commit()

conn.close()