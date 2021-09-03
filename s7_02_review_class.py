# The example below is something Helena came up with to show what happens
# when self is not used in a class. Possible use-case: when objects created
# on a certain day should have that date as an attribute. So, depending on
# the day a bunch of objects were created from a class, they will all
# share the same date.

# I think the following explains OOP well and hopefully clarifies
# what we have been doing with classes.
# https://realpython.com/python3-object-oriented-programming/
# My favorite sentences from that post are:
# "OOP models real-world entities as software objects that have some data
# associated with them and can perform certain functions."
# and
# "Classes are used to create user-defined data structures. Classes define
# functions called methods, which identify the behaviors and actions that
# an object created from the class can perform with its data."

# Let's make a class that has a function and attribute without self.
import random
class User:

    def generate_salt1():
        return random.randint(0,10000)

    salt1 = generate_salt1()

    def generate_salt2(self):
        self.salt2 = random.randint(0,10000)

# >>> import s7_02_review_class
# >>> from s7_02_review_class import User
# >>> User.salt1 # This value is created at runtime, when we import User.
# >>> User.generate_salt1() # Calling the function using the class calculates
# a new random number, but it does not equal the attribute salt1 created
# at runtime.
# >>> User.salt1
# >>> User.salt2 # doesn't exist yet, since it is created with the
# generate_salt2 method.
# Okay, let's call the function
# >>> User.generate_salt2() # !!!!! Error message!!!! It needs an object,
# aka an instance of the class to refer to. It needs a "self".

# Let's look at the type of User and an instance of User called user1.
# >>> type(User)
# <class 'type'>
# >>> user1 = User()
# >>> type(user1)
# <class 's7_02_review_class.User'>
# By creating an instance of the class User, we have an object (a self) and
# can now create a salt2 attribute.
# >>> user1.generate_salt2()
# >>> user1.salt2
# >>> user1.salt1 # the class instance has inherited salt1 from the class User.
# >>> user1.salt1 += 1 # we change the attribute salt1 in the user1 object,
# but the class salt1 (User.salt1) is still the original.
# >>> User.salt1 += 22 # we can change the class level salt1 and all new objects
# will have this new value, since we assigned it in the class's scope.
# >>> user2 = User()
# >>> user2.salt1 # Note that user2's salt1 is the original salt1 plus 22.
