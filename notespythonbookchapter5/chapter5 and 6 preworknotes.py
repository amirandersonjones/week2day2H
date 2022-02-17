alien_color = 'green'
if alien_color == 'green':
    print("you earned 5 points")

alien_color = 'yellow'
if alien_color == 'green':
    print("you earned 5 points")

alien_color = 'red'
if alien_color == 'green':
    print("you earned 5 points")
else:
    print("you earned 10 points")

alien_color = 'red'
if alien_color == 'green':
    print("you earned 5 points")
if alien_color == 'red':
    print("you earned 10 points")

#If the alien is green, print a message that the player earned 5 points.
#If the alien is yellow, print a message that the player earned 10 points.
#If the alien is red, print a message that the player earned 15 points.
#Write three versions of this program, making sure each message is printed 
#for the appropriate color alien

alien_color = 'red'
if alien_color == 'green':
    print("you earned 5 points")
if alien_color == 'yellow':
    print("you earned 10 points")
if alien_color == 'red':
    print("you earned 15 points")

#IF STATEMENTS WITH LISTS

    #Checking for special items within a list:
    # A simple "FOR LOOP" that prints a message for every topping requested

requested_toppings = ['pepperoni','cheese','mushroom']
for requested_topping in requested_toppings:   #requested_topping is a placeholder variable
    print("Adding your" + " " + requested_topping)
print("\nFinished making your pizza!")
#The loop reads for every requested_topping in the list of requested_toppings  print the 2 
#that follow.

#But what if there is a special circumstance like running out of mushrooms?
#Using an IF STATEMENT in a FOR LOOP will address that:

requested_toppings = ['pepperoni','cheese','mushroom']
for requested_topping in requested_toppings:
    if requested_topping == 'mushroom':
        print("Im sorry we are out of" + " " + requested_topping)
    else:
        print("Adding" + " " + requested_topping)

#To CHECK IF A LIST IS EMPTY
# let’s check whether the list of requested toppings is 
#empty before building the pizza. If the list is empty, we’ll prompt the user 
#and make sure they want a plain pizza. If the list is not empty, we’ll build 
#the pizza just as we did in the previous examples

requested_toppings = [] 
if requested_toppings:   
    for requested_topping in requested_toppings:  #python reads this as:if there is something in the list requested_toppings it will return TRUE if the List is empty it will return FAlSE.
        print("Adding" + requested_topping)
else:
    print("Are you sure you want a plain pizza?")

#USING MULTIPLE LISTS
#For example, checking one list of available toppings against a list of requested toppings
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple','extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding" + " " + requested_topping)
    else:
        print("I'm sorry we don't have that topping:" + requested_topping)

#5-8. Hello Admin: Make a list of five or more usernames, including the name 
#'admin'. Imagine you are writing code that will print a greeting to each user 
#after they log in to a website. Loop through the list, and print a greeting to 
#each user:
#•	 If the username is 'admin', print a special greeting, such as Hello admin, 
#would you like to see a status report?
#•	 Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.

names_list = ['admin', 'Kellie', 'Jase', 'Sue', 'Beth']
for name in names_list:
    if name == 'admin':
        print("hello" + " " + name + " " + "you are the admin" + " " + "would you like to see a status report?")
    else:
        print ("hello" + " " + name)

names_list = ['Kellie']
if names_list:
    for names in names_list:
        print("Hello" + " " + names)
else:
    print("we need user!")

#PREWORK NOTES-Kevin Video

#BOOLEAN-can be 2 things. True or False or Yes or No
#bool()-will convert something into a boolean. print(bool(0))=False 
# print(bool(1))-True. Any number that is not zero is True and zero is False.
#print(bool("")) to check if a string is empty. print(bool([]).)
#print(ord("A"))-to see what the ASKI number value is that is associated with the letter.
#FOR LOOP is sequential. IF STATEMENT is CONDITIONAL. WHILE STATEMENT is LOOPING.

#IF STATEMENT

#IF BOOLEAN OR BOOLEAN EXP:
    #CODE BLOCK
    # FOR IF TRUE
#ELSE:
    #FOR THE IF FALSE CODE BLOCK

height = 65

#Must be 5 feet tall to ride my ride
#Must be under 6 feet tall to ride

if height  < 60:
    print("you are too short")
    print("I am sorry, but get off of my ride!")
elif height > 72:
    print("you are too tall")
    print("get off my ride")
else:
    print("Enjoy the ride!")

print("thanks for visiting") #This is outside of the codeblock and prints regardless



#DICTIONARIES

#A dictionary in Python is a collection of key-value pairs. Each key is connected 
#to a value, and you can use a key to access the value associated with that key. 
#A key’s value can be a number, a string, a list, or even another dictionary. 
#In fact, you can use any object that you can create in Python as a value in a 
#dictionary.
    # In Python, a dictionary is wrapped in braces, {}, with a series of key 
    # value pairs inside the braces, as shown in the earlier example

alien_0 = {'color':'green', 'points': 5}

#A key-value pair is a set of values associated with each other. When you 
#provide a key, Python returns the value associated with that key. Every key 
#is connected to its value by a colon, and individual key-value pairs are separated by commas. 
# You can store as many key-value pairs as you want in a dictionary.

#ACCESSING THE DICTIONARY - To get the value associated with a key, give the name of the dictionary 
# and then place the key inside a set of square brackets, as shown:

alien_0 = {'color':'green', 'points': 5}
print(alien_0['color'])

#Once the dictionary has been defined, the code at u pulls the value 
#associated with the key 'points' from the dictionary. This value is then 
#stored in the variable new_points. The line at v converts this integer value 
#to a string and prints a statement about how many points the player just earned

#If you run this code every time an alien is shot down, the alien’s point 
#value will be retrieved:
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#ADDING NEW KEY/VALUE PAIRS
alien_0 = {'color':'green', 'points': 5} #OLD DICTIONARY
print(alien_0['color'])

alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)

#ADDING TO AN EMPTY DICTIONARY

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points']= 5
print(alien_0)

#MODIFYING A DICTIONARY
alien_0 = {'color':'green', 'points':5}
print("the color of your alien is" + " " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("your new alien color is" + " " + alien_0['color'] + ".")

my_dic= []
print(my_dic)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Your original alien x position is:" + " " + str(alien_0['x_position']))

#Now we are going to:
    # Move the alien to the right.
    # Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0 ['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
 # The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("The new alien x position is:" + str(alien_0['x_position']))

#REMOVING KEY VALUE PAIRS
    #Be aware that the deleted key-value pair is removed permanently.
alien_0 = {'color':'green', 'points':5}
print(alien_0)

del alien_0['points']
print(alien_0)

#A DICTIONARY OF SIMILAR OBJECTS:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("Jen's favorite languages is" + "" + "" + favorite_languages['jen'].title() + ".")

#6-1. Person: Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live. You 
#should have keys such as first_name, last_name, age, and city. Print each 
#piece of information stored in your dictionary.

Kellie_info = {
    'first_name': 'kellie',
    'last_name': 'chandler',
    'sex': 'female',
    'born': 'chicago',
    }
print(Kellie_info['born'])
print(Kellie_info['first_name'])
print(Kellie_info['sex'])

#LOOPING THROUGH A DICTIONARY
#Dictionaries can be used to store information 
#in a variety of ways; therefore, several different ways exist to loop through 
#them. You can loop through all of a dictionary’s key-value pairs, through its 
#keys, or through its values.

    #looping through all key value pairs(FOR LOOP):
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
    print("\nkey:" + key)
    print("value" + value)
#As shown at , to write a for loop for a dictionary, you create names for 
#the two variables that will hold the key and value in each key-value pair. You 
#can choose any names you want for these two variables. This code would work 
#just as well if you had used abbreviations for the variable names, like this:
#k instead of key and v instead of value.

#The second half of the for statement at u includes the name of the dictionary followed 
# by the method items(), which returns a list of key-value pairs. 
#The for loop then stores each of these pairs in the two variables provided.

#The "\n" in the first print statement ensures that a 
#blank line is inserted before each key-value pair in the output:
    
    #looping through all of the keys in a key value pair(FOR LOOP):

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in favorite_languages.keys():
    print(name.title())

#To check in see if a particular name is in the list?
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
     'phil': 'python',
     }
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

#To sort names in a dictionary 
#One way to return items in a certain order is to sort the keys as they’re 
#returned in the for loop. You can use the sorted() function to get a copy of 
#the keys in order:

for name in sorted(favorite_languages.keys()):
    print(name.title() + " " + "Thank you for taking my survey" )

    #looping through the values of a dictionary using the FOR LOOP:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for value in sorted(favorite_languages.values()):
    print(value.title())

#To avoid repetition of information in large dictionaries you can use the set() method 
#The result is a nonrepetitive list of languages that have been mentioned 
#by people taking the poll:

#DEVON'S TUTORIAL NOTES FOR CREATING A FUNCTION
#take in a number and divide by 5

def times_five(n):
    return 'n * 5'
times_five(8)


#take in 5 names and repeat them

def names(f_name):
    name=[]
    for n in f_name: 
        name.append(n)
    print(name)
names(['Eric','Bill', 'Socrates','Kellie', 'Dave'])

#Given a list as a parameter,write a function that returns a list of numbers that are less than ten
#For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

