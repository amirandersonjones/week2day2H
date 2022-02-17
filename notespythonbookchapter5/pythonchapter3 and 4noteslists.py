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

#Doing Something After a for Loop