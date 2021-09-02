from os import close
import sqlite3, tkinter
from sqlite3.dbapi2 import Cursor, connect
from tkinter import font

with sqlite3.connect("user_data.db") as db:
    cursor = db.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    first_name text,
    last_name text,
    age integer,
    username text,
    password text
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



main_window=tkinter.Tk()
main_window.title('VeloCity')
main_window.geometry('1600x900')
padd=40
main_window['padx']=padd
info_label=tkinter.Label(main_window, text='VeloCity Login')
info_label.grid(row=0, column=0)

info_user=tkinter.Label(main_window, text='username')
info_user.grid(row=1, column=0)
userinput=tkinter.Entry()
userinput.grid(row=1, column=1)

info_pass=tkinter.Label(main_window, text='password')
info_pass.grid(row=2, column=0, pady=20,)
passinput=tkinter.Entry()
passinput.grid(row=2, column=1)

login_btn=tkinter.Button(text='Login')
login_btn.grid(row=3, column=1)







menu()

close




db.close()