# This lesson is based on following the dbahn_api_instructions and
# getting an individual authentication key. The proper way to share code that
# requires authorization is by having a separate file for each person
# from which the authorization details get loaded.

# I didn't do that in class, but I will do it here. Create a file in the same
# directory as this file called auth.key. The one and only line of code
# in the file with be your authentication key.

# I started at the command line in class, pulling all the elements together
# to create a recommendation system for trips. These are the pieces we needed
# to get:
# 1. Data about audo media with a certain length. Y'all supplied that, thanks!
# 2. A way to determine trip duration. We use the Deutsche Bahn api to get it.
# The first thing was to figure out how to get duration out of the api. To do
# this, I went step by step through the different commands explained in the
# api documentation. This is found at the url from Step 2 of the instructions,
# click on the API CONSOLE tab.

import requests, json # the packages we need for this code.

# The proper way to pull in authorization secrets.
# Note that you need a space between Bearer and the variable.
with open('auth.key','r') as f:
    auth_key = f.readline().replace('\n','')
# Create the headers variable to be used later in the requests.get function.
headers = {"authorization": f"Bearer {auth_key}"}

# Based on the api, the first thing we can do is get info about a location.
# Let's do that and see what gets returned.
# We need to create the url where the information we need is located. From
# the documenation, we know there is a base part of the url and then a separate
# part that changes, depending on what info we want to get. So, we can set base
# and then keep reusing it with the different commands.
base = "https://api.deutschebahn.com/fahrplan-plus/v1/"
command1 = "location/lueneburg"
url1 = base + command1
# To pull the actual data, we send out a request to the api, like so:
response1 = requests.get(url1,headers = headers).json()

# Let's inspect the response
type(response1) # it is a list, so we can index it to see what it contains.
type(response1[0]) # we see that response is a list of dictionaries.
response1[0].keys() # by getting the keys, we see the kind of info we have.

# From the documentation, we see that times are located in journey details.
# We need to find particular ids to get those details. But first, we need to
# pick one journey to get the journey details for.
# Let's start with Lueneburg. We need it's id.
id = response1[0]['id']
# Now we look in the arrivals board for Lueneburg, using the id.
command2 = f"arrivalBoard/{id}?date=2021-06-29T12:00"
url2 = base + command2
response2 = requests.get(url2,headers = headers).json()
# Let's take the first train from the response and use that detailsId.
detailsId = response2[0]['detailsId']

# Now, with the detailsId of the journey we can finally get the departure time
# from the origin location and the arrival time from the destination. In this
# case, it is Stuttgart and Lueneburg.
# BUT!!!!! The details ID has a % sign in it, which is a special character
# for urls. I liked the following explanation:
# https://secure.n-able.com/webhelp/NC_9-1-0_SO_en/Content/SA_docs/API_Level_Integration/API_Integration_URLEncoding.html

# To code an actual percent sign in a URL, the code is %25,
# so all % need to be replaced with %25. How did I figure this out? Well,
# using the details_id, I kept getting a json encoding error. That means,
# the url is formatted wrong. For example, several of you also got that in
# class when a / was missing. I then looked at the API CONSOLE and used the "try it out"
# button, which returned the properly formatted url. (Note you have to put an id
# in the request field.)
f_detailsId = detailsId.replace('%','%25')
command3 = f"journeyDetails/{f_detailsId}"
url3 = f"https://api.deutschebahn.com/fahrplan-plus/v1/{command3}"
response3 = requests.get(url3,headers = headers).json()

# Inspect response3. Note that there are arrTime and depTime for each
# stop on the journey, except the first and last. We need a list of the
# times to calculate the depature time from Stuttgart and the arrival time
# in Lueneburg. You could use a try / catch or an if conditional statement.

a_list = []
for i in response3:
    try:
        a_list.append((i['depTime']))
    except:
        a_list.append((i['arrTime']))

# Inspect a_list. We now have strings of the times, but we can't do mathematical
# calculations on string. Therefore, we need to change them into time data
# types to be able to do calculations in base 60. We do that using the
# datetime package. Check out the documentation on how to use it.
from datetime import datetime
start = datetime.strptime(a_list[0], '%H:%M')
end = datetime.strptime(a_list[-1], '%H:%M')
tdelta = end - start
len_minutes = tdelta.seconds / 60

# The last piece left to get are the recommendations y'all created.
# This is simply reading in the file. Make sure the file is either in
# the directory you are working in, or you can put in the full path of the file.
import csv
file = 'tb1_recommendations.csv'
fieldnames = ['title','media','duration','mood']
with open(file,'r',encoding='utf-8') as f:
    f.readline()
    reader = csv.DictReader(f, delimiter=',', fieldnames=fieldnames)
    data = [row for row in reader]

# AND FINALLY! We can get suggestions. Note that the trip is so long, all
# options are suggestions. Change len_minutes to something shorter, like 20,
# and you will see the suggestions change.
suggestions = []
for i in data:
    if int(i['duration']) < int(len_minutes):
        suggestions.append(i['title'])

# EXERCISE
# A) add mood as an option
suggestions = []
for i in data:
    if int(i['duration']) < int(len_minutes) and i['mood'] == 'happy':
        suggestions.append(i['title'])
# B) Create a class to make suggestions, using the algorithm we did in class.
# my answer is trip_reco.py. Yes, this is rather complicated. It took me over
# an hour to write and test, but it may serve as a template for when you need
# to do something similar for your assignment.

### IF THERE IS TIME
# Show how to sort on a different position using lambda.
# Let's say the data wasn't returned in time order and we wanted to
# see the stations along the route. We would create a list like this:
a_list = []
for i in response:
    try:
        a_list.append((i['stopName'], i['depTime']))
    except:
        a_list.append((i['stopName'], i['arrTime']))

# And then we would need to sort to make sure we get the first and last stops
# on the route.

# There are several options - you could write your own sorting algorithm,
# use the .sort method on a list or use the built-in sorted function.
# The way I set up the list, the element we want to sort by is the second element.
# Therefore, we need a trick to sort along the second element, not the first.
# Another option is to build the list with time as the first element or
# just have a list of times, as we did in class, since that is all we need.
# However, let's say these weren't options and we had to sort on the second
# element.
# https://www.geeksforgeeks.org/python-program-to-sort-a-list-of-tuples-by-second-item/
# https://www.geeksforgeeks.org/sort-in-python/
sorted_list = sorted(a_list, key = lambda x: x[1])
a_list.sort(key = lambda x: x[1]) # This is done inplace. And we are done, the
# list is sorted along the second element.

# BUT OMG! What is this lambda?!?!?! It is a way to write a function in one line.
def sort_second(x):
    return x[1]
# is the same as
lambda x: x[1]
# This is used a lot in python, so now you know!
