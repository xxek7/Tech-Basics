import sqlite3

conn = sqlite3.connect('users.db')

#create a cursor
c = conn.cursor()

#create a table
#c.execute("""CREATE TABLE users (
 #   first_name text,
  #  last_name text,
   # email text
#)""")

#many_users = [
 #               ('Johanna', 'Frank', 'frank@web.de'),
  #              ('Bjarne', 'Voss', 'voss@web.de'),
   #             ('Henrike', 'Bahr', 'bahr@web.de'),
    #            ('Maurice', 'Heel', 'heel@web.de'),
     #           ('Joni', 'Sierks', 'sierks@web.de'),
      #          ('Jonny', 'Floeter', 'jojo@web.de')

         #   ] 

#c.executemany("INSERT INTO users VALUES (?,?,?)", many_users)



#Update Records
#c.execute("""UPDATE users SET first_name = 'Bjarne Leon'
 #           WHERE rowid = 5
    

#""")

#Delete Records
#c.execute("DELETE from users WHERE first_name = 'Bjarne Leon'")

#conn.commit()



c.execute("SELECT rowid, * FROM users")
                                                #mögliche operatoren:
                                                #= < > ...
                                                #LIKE '...'

items = c.fetchall()


for item in items:
    print(item)
    #print(item[0] + " " + item[1] + "\t" + item[2])









#commit our command
conn.commit()

#close connection
conn.close