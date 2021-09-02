from os import close
import sqlite3
from sqlite3.dbapi2 import Cursor, connect

with sqlite3.connect("user_data.db") as db:
    cursor = db.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    username TEXT,
    password TEXT
    )
''')

db.commit()

def register():
    firstname = input("please enter your first name: ")
    lastname = input("please enter your last name: ")
    age = input("Please enter your age: ")


    free = 0
    while free ==0:
        username = input("please choose a username: ")
        with sqlite3.connect("user_data.db") as db:
            cursor = db.cursor()
        findUser = ("SELECT * FROM users WHERE username = ?")
        cursor.execute(findUser,[(username)])

        if cursor.fetchall():
            print("Username already taken, please enter a different one")
        else:
            free = 1


    password = input("please choose a password: ")


    user = [ (firstname, lastname, age, username, password) ]

    cursor.executemany("INSERT INTO users VALUES (?,?,?,?,?)", user)

    db.commit()

    print("Registration successful")

    menu()



def login():
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        with sqlite3.connect("user_data.db") as db:
            cursor = db.cursor()
        findUser = ("SELECT * FROM users WHERE username = ? AND password = ?")
        cursor.execute(findUser,[(username), (password)])

        if cursor.fetchall():
            print("Login successful")
            break
        else:
            print ("username or password incorrect, please try again")


def menu():
    status= input("Welcome to VeloCity, what would you like to do? register/login:  ")
    if status == "register":
        register()
    elif status == "login":
        login()
    else:
        print("Please enter a valid command")



menu()

close




db.close()