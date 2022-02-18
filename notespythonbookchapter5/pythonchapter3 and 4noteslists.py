#defining your list
bicycles = ['trek', 'cannondale','redline', 'specialized'] 

#Printing a particular item from your list and using string methods() to modify the print output
print(bicycles[1])
print(bicycles[0].title())
print(bicycles[-1].upper())
print(bicycles[-1].lower())

#Printing items from the list using string concatenation
print("My first bicycle was a" + " " + bicycles[0].title() + ".")

#Changing items in a list
friends = ['Tommy', 'Jill', 'Kellie', 'Bob']
print("Hi" + " " + friends[0])
print(friends)
friends[0] = 'Jeannette'
print(friends)

#The simplest way to add a new element to a list is to append the item to the 
#list. When you append an item to a list, the new element is added to the end 
#of the list. 

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)

print(motorcycles[1])

#Inserting items into a LIST
#You can add a new element at any position in your list by using the insert()
#method. You do this by specifying the index of the new element and the 
#value of the new item.

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(2, 'ducati')

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(2, 'ducati')
print(motorcycles)

#REMOVING items from a LIST
del motorcycles[2]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

#Removing an Item Using the pop() Method
#The pop() method removes the last item in a list, but it lets you work 
#with that item after removing it.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(3,'ducati')
print(motorcycles)

print(popped_motorcycles)

motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

del motorcycles[1]

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
del motorcycles[3]
print(motorcycles)
motorcycles.insert(3,'ducati')
print(motorcycles)
print(popped_motorcycles)
popped_motorcycles = ''
print(popped_motorcycles)
print(motorcycles)
motorcycles.pop(2)
print(motorcycles)
print("The first motorcycle I owned was a" + popped_motorcycles + "!")

#Removing an Item by Value
# Sometimes you won’t know the position of the value you want to remove 
# from a list. If you only know the value of the item you want to remove, you 
# can use the remove() method.
# For example, let’s say we want to remove the value 'ducati' from the list of motorcycles.

print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

#You can also use the remove() method to work with a value that’s being 
# removed from a list. Let’s remove the value 'ducati' and print a reason for 
# removing it from the list
#The remove() method deletes only the first occurrence of the value you specify. If there’s 
#a possibility the value appears more than once in the list, you’ll need to use a loop to 
#determine if all occurrences of the value have been removed. 

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print("I didnt want my" + " " + too_expensive + " " "it cost too much!")

dinner_invite= ['mom','dad','kellie','tommy']
print(dinner_invite)

del dinner_invite[3]
print(dinner_invite)
dinner_invite.insert(3,'tommy')
print(dinner_invite)



print(dinner_invite)
popped_dinner_invite = dinner_invite.pop()
print(popped_dinner_invite)
print("Unfortunately" + " " + popped_dinner_invite + " " + "wont be making it!")

print(dinner_invite)
dinner_invite.insert(3,'bro')
print(dinner_invite)

dinner_invite.pop()
print(dinner_invite)

#SORTING A LIST
    #Sorting a List Permanently with the sort() Method-The sort() method, shown at u, changes the order of the list permanently. The cars are now in alphabetical order, and we can never revert to 
    #the original order.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
    #sorting the list in reverse-Again, the order of the list is permanently changed.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

    #Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print("Here is the original list")
print(sorted(cars))
print("\nHere is the sorted list")
print(cars)

#Finding the Length of a List-You can quickly find the length of a list by using the len() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

#LOOPING THROUGH A LIST-Looping allows you to take the same action, or set of actions, 
# with every item in a list. As a result, you’ll be able to work efficiently with 
# lists of any length, including those with thousands or even millions of items

#FOR LOOP IS USED WHEN YOU WANT TO TAKE THE SAME ACTION FOR EVERY ITEM IN A LIST
#The concept of looping is important because it’s one of the most common 
# ways a computer automates repetitive tasks. 

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians:
    print(magician)


#When you’re using loops for the first time, keep in mind that the set of 
# steps is repeated once for each item in the list, no matter how many items 
# are in the list. If you have a million items in your list, Python repeats these 
#steps a million times—and usually very quickly.
#Also keep in mind when writing your own for loops that you can choose 
#any name you want for the temporary variable that holds each value in the 
#list. However, it’s helpful to choose a meaningful name that represents a 
#single item from the list. 

magicians = ['alice', 'david', 'carolina'] 
print(magicians)
for magician in magicians:
    print("That was a really good trick" + " " + magician.title())
    print(magician.title() + " " + "I cant wait to see your next trick!\n")
print("Thanks to everyone for their participation")

#You can also write as many lines of code as you like in the for loop. 
#Every indented line following the line for magician in magicians is considered inside the loop, 
# and each indented line is executed once for each 
#56 Chapter 4 value in the list. Therefore, you can do as much work as you like with 
# each value in the list.

#Making Numerical Lists
#Using the range() Function-In this example, range() prints only the numbers 1 through 4. 
    # This is another result of the off-by-one behavior you’ll see often in programming 
    #languages. The range() function causes Python to start counting at the first 
    #value you give it, and it stops when it reaches the second value you provide. 
    #Because it stops at that second value, the output never contains the end 
    #value, which would have been 5 in this case.

for value in range(1,11):
    print(value)

for number in range(1,21):
    print(number)

    print("hello")
for number in range(1,21):
    print(number)

#Using range() to Make a List of Numbers
my_favorite_numbers = list(range(1,10))
print(my_favorite_numbers)
for numbers in range(8,11):
    print(numbers)
my_favorite_numbers = list(range(20,41))
print(my_favorite_numbers)

for numbers in range(1,5):
    print(numbers)

my_list = list(range(1,10))
print(my_list)

odd_numbers = list(range(1,11,2))
print(odd_numbers)

#create a list of the first ten numbers squared.
#create a list of 1-10
#square the numbers using **2
#print the list of numbers

squares=[] #create an empty list of squares
for value in range(1,11): #for loop to cycle through all the #'s we need squared.spaure 1-12
    square = value**2 #here we state what we will be doing as we cycle the for loop
    squares.append(square) #this statement read append the square to the list of squares
print(squares)

squares = []
for value in range(1,11):
    square = value **2
    squares.append(square)
print(squares)

for value in range(1-9):
    print(value)

my_bif_list= list(range(2,11,2))
print(my_bif_list)

#PERFORMING SIMPLE STATS ON LISTS: MIN/MAX/SUM
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

for values in range(9, 31):
    print(values)

my_dog= list(range(9,13))
print(my_dog)

for value in range(100, 113):
    print(value)

my_tote= list(range(1,16))
print(my_tote)

for values in range(1,9):
    print(values)

#LIST COMPRHENSION-A list comprehension allows you to generate 
#this same list in just one line of code. A list comprehension combines the 
#for loop and the creation of new elements into one line, and automatically 
#appends each new element. 

squares= [value** 2 for value in range (1, 11)]
print(squares)

for value in range(1, 21):
    print(value)

a_million= list(range(1, 100000))
print(max(a_million))
print(min(a_million))
print(sum(a_million))

for values in list(range(1,21,2)):
    print(values)

for values in list(range(3,31,3)):
    print(values)

squares= []
for values in range(1,21):
    square = values **2
    squares.append(square)
print(squares)

cubes=[]
for values in range(1,11):
    cube=values**3
    cubes.append(cube)
print(cubes)

cubes=[value**3 for value in range(1,21)]
print(cubes)

#SLICING-To make a slice, you specify the index of the first and last elements you 
#want to work with. As with the range() function, Python stops one item 
#before the second index you specify.

players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3])

#CHAPTER 7 WHILE LOOPS AND USER INPUT
#You’ll use Python’s while loop to keep programs running as long as certain conditions remain true.
#THE INPUT FUNCTION = input()
message= input("Tell me something about yourelf and I'll repeat it:")
print(message)

#The input() function pauses your program and waits for the user to enter 
#some text. Once Python receives the user’s input, it stores it in a variable to 
#make it convenient for you to work with.
#PROMPTS
    #Sometimes you’ll want to write a prompt that’s longer than one line. For 
    #example, you might want to tell the user why you’re asking for certain input. 
    #User Input and while Loops 119
    #You can store your prompt in a variable and pass that variable to the input()
    #function. This allows you to build your prompt over several lines, then write 
    #a clean input() statement.


prompt = "I promise I wont do anything with your personal information."
prompt += "\nWhat is your first name?"
name = input(prompt)
print("\n Hello" + " " + name + "!")

address = input("What is your address?:")
address_prompt = "We only use your address for shipment info!"
address = input(address_prompt)


print("\nThanks for entering your address!")

#Using int() to Accept Numerical Input
#When you use the input() function, Python interprets everything the user enters as a string
# When you try to use the input to do a numerical comparison u, Python 
#produces an error because it can’t compare a string to an integer: 
#We can resolve this issue by using the int() function, which tells 
#Python to treat the input as a numerical value. The int() function converts a 
# string representation of a number to a numerical representation, 
#as shown here:

age=input("How old are you?")
age=int(age)
print(age)

age > 18
print(True)

height= input("How tall are you?")
height=int(height)
if height >= 44:
    print("\nYou are tall enough for this ride!")
else:
    print("\nYou're not tall enough!")

number=input("Please enter a number here.")
number=int(number)
if number % 2 ==0:
    print("This number is even!")
else:
    print("This number is odd!")

#THE WHILE LOOP
#The for loop takes a collection of items and executes a block of code once 
#for each item in the collection. In contrast, the while loop runs as long as, 
#or while, a certain condition is true.

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program.
message = " "