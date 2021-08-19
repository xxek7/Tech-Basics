users = {}
status = ""

def displayMenu():
    status = input ("Are you registered user? y/n?")
    if status == "y":
        oldUser()
    elif status =="n":
        newUser()

def newUser() :
    createLogin = input ("Create login name")

    if createLogin in users:
        print ("\nLogin name already exist!\n")
    else:
        createPassW = input ("Create Password ")
        users[createLogin] = createPassW
        print ("\nUser created\n")

def oldUser() :
    login = input ("Enter login name: ")
    passw = input ("Enter password: ")

    if login in users and users[login] == passw:
        print ("\nLogin succesful!\n")
    else:
        print ("\nUser doen't exist or wrong password!\n")

while status != "q":
    displayMenu()