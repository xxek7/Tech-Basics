from os import close, stat
import sqlite3, os
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


def menu():
    status= input('''
    Welcome to VeloCity, choose any of the options below
    r to register
    l to login
    q to quit  
    ''')
    if status == "r":
        register()
    elif status == "l":
        login()
    elif status == "q":
        quit()
    else:
        print("Please enter a valid command")


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

    os.chdir("users")
    os.mkdir(username)
    os.chdir(username)

    with sqlite3.connect("user_bikes.db") as db:
        cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bikes (
        type TEXT,
        tire size INTEGER,
        frame size INTEGER,
        sex TEXT,
        color TEXT
        )
    ''')
    db.commit()

    os.chdir("..")
    os.chdir("..")

    print("Registration successful, please login again")

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
            os.chdir("users")
            os.chdir(username)

            print("Login successful")

            dashboard()
        else:
            print("username or password incorrect, please try again")


def dashboard():
    option = input('''
    Welcome to VelCity, the innovative bike-sharing platform
    This is your Account dashboard,
    please select from the following:

    a to add a new bike you would like to share
    s to show all your bikes
    l to log out
    q to quit 
    ''')
    if option == "a":
        add_bike()
    elif option == "s":
        show_bikes()
    elif option == "l":
        os.chdir("..")
        os.chdir("..")
        menu()
    elif option == "q":
        quit()
    else:
        print ("please enter a valid command")

       
def add_bike():
    with sqlite3.connect("user_bikes.db") as db:
        cursor = db.cursor()

    type = input("what type is your bike?")
    tire_size = input("please enter the tire size")
    frame_size = input("please enter the frame size")
    sex = input("please choose between 'male', 'female' or 'unisex'")
    color = input("please enter the color of the bike")

    bike = [ (type, tire_size, frame_size, sex, color) ]
                
    cursor.executemany("INSERT INTO bikes VALUES (?,?,?,?,?)", bike)

    db.commit()

    print("Bike successfully added!")

    option = input('''
    press 'a' to add a new bike you would like to share
    press 'b' to go back to your dashboard
    ''')
    if option == "a":
        add_bike()
    elif option == "b":
        dashboard()


def show_bikes():
    with sqlite3.connect("user_bikes.db") as db:
        cursor = db.cursor()
    
    cursor.execute("SELECT * FROM bikes")

    bikes = cursor.fetchall()
    for item in bikes:
        print(item)

    dashboard()


menu()

close

db.close()