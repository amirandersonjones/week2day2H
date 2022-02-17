#CONDITIONAL STATEMENTS-can be evaluated as True or False by python. If the statement is TRUE
#then it runs the code block in an IF statement. If it's FALSE then python ignores the code.

#CONDITIONAL STATEMENTS:
    #1.)Equality test- variable == value of the thing of interest
        #car = 'bmw' sets the car variable to 'bmw'/set the value of car equal to 'bmw'
        #car == 'bmw' checks whether the value of car is equal to 'bmw' This statement would return TRUE
        #car.lower() == 'bmw'- would check for the value of car whether entered lowercase or uppercase.
    #2.)Inequality test- !=
        #  requested_topping = 'mushrooms'
        # if requested_topping != 'anchovies': Returns TRUE and therefore prints the block of code following
        #print("Hold the anchovies!")
    #3.)Mathematical comparisons->,<, <=, =>, and, or to check multiple conditions
    #4.)Checking to see if something is in the list and returning TRUE or FALSE

requested_toppings = ['mushroom', 'pepperoni', 'sausage']
'mushrooms' in requested_toppings #TRUE
print(True)
input = 'olives' 
if input not in requested_toppings: #TRUE
    print(True)
input = 'mushrooms'
if input in requested_toppings: #TRUE
    print(True)
input = 'olives'
if input in requested_toppings: #FALSE
    print(True) #will not execute
    #5.)Boolean Expressions-Boolean values are either TRUE or FALSE.
        # game_active = True
        #can_edit = False
        #Boolean values provide an efficient way to track the state of a program 
        #or a particular condition that is important in your program

#IF STATEMENTS-TEST 1 CONDITION-When you understand conditional tests, you can start writing if statements. 
#Several different kinds of if statements exist, and your choice of which to 
#use depends on the number of conditions you need to test.
    #1.)Simple IF statements have one step
        #if conditional_statement-can be any conditional test
            #do something-if the conditional statement is TRUE python runs idented code. 
            #If FALSE it is ignored.
            #identation is VERY important. All idented lines of text will execute if TRUE/IGNORED
            #if FALSE.
age = 19
if age >= 19: #TRUE
    print("Gee, you're very young!") #will execute

age = 19
if age <= 10: #FALSE
    print("You're getting older!") #wont execute producting NO OUTPUT!

#IF-ELSE STATEMENTS-TEST 2 CONDITIONS-Often, you’ll want to take one action when a conditional test passes and a 
# different action in all other cases.allows you to define an action or set of actions 
# that are executed when the conditional test fails.

age = 15
if age <= 11:  #TRUE
    print("You may attend the party!")
else:
    print("You're too old to be here!")

#IF-ELIF-ELSE STATEMENTS-TEST MORE THAN 2 CONDITIONS-Python executes only one 
#block in an if-elif-else chain. It runs each conditional test in order until 
#one passes. When a test passes, the code following that test is executed and 
#Python skips the rest of the tests.
#Admission for anyone under age 4 is free. Admission for anyone between the ages of 4 and 18 is $5.
# Admission for anyone age 18 or older is $10

age = 15
if age < 4:  #False
    print("your cost of admission is FREE")
elif age < 18: #True
    print("your cost of admission is $5")
else:  #False
    print("your cost of admisstion is $10")
#simple more modified version of If-ELIF-ELSE statement
age = 15
if age < 4:
    admision = 0
elif age < 18:
    admission = 5
else:
    admission = 10

print("your admission is $" + str(admission) + ".")

    #The ELSE block is a a catchall statement. It matches any condition that 
    #wasn’t matched by a specific if or elif test, and that can sometimes include 
    #invalid or even malicious data. If you have a specific final condition you are 
    #testing for, consider using a final elif block and omit the else block. As a 
    #result, you’ll gain extra confidence that your code will run only under the 
    #correct conditions.
age = 12
if age < 4:
 price = 0
elif age < 18:
 price = 5
elif age < 65:
 price = 10
elif age >= 65:
 price = 5
print("Your admission cost is $" + str(price) + ".")

#When you need ALL CRITERIA TO BE TESTED you should use multiple "IF" statements instead of using
#IF-ELIF-ELSE-sometimes it’s important to check all of the conditions of 
# interest. In this case, you should use a series of simple if statements with no 
# elif or else blocks. This technique makes sense when more than one condition 
# could be True, and you want to act on every condition that is True. OTHERWISE in an IF-ELIF-ELSE
# statement as soon as one condition passes the program will stop executing.

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
 
print("\nFinished making your pizza!")

l_1 = [1,11,14,5,8,9]
def lessthanten(numbers):
    new_numbers = []
    for n in numbers:
        if n < 10:
            new_numbers.append(n)
    return new_numbers

l_1 = [1,2,3,4,5,6]     
l_2 = [3,4,5,6,7,8,10]

def mergelist(list1, list2):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i] + ' ' + list2[i])
    return new_list
#should work for any two lists of consistent datatype


l_1 = [1,11,14,5,8,9]

def lessthanten(numbers):
    new_numbers = []
    for n in numbers:
        if n < 10:
            new_numbers.append(n)
    return new_numbers
print(lessthanten([1,11,14,5,8,9]))


#Consecutive Indices
#You are given a list of unique integers (arr), and two integers (a and b). 
# Your task is to find out whether or not a and b appear consecutively in arr, 
# and return a boolean value (True if a and b are consecutive, False otherwise).
#It is guaranteed that a and b are both present in arr.
#Example:
#Input: ([1, 6, 9, -3, 4, -78, 0], -3, 4)
#Output: True
#Input: ([3,1,0,19], 19, 0)	
#Output: True

#to solve this think about 2 inputs. 1.)list 2.)integer a 3.)integer b
#if you get the index of integer 1 the second one would be +1 or -1
#absolute value-avoid it being a bug in code. ignore whether the number is positive or negative.

def consecutive(list, a, b):
    index_1 = list.index(a)
    index_2 = list.index(b)
    test = abs(index_1 - index_2)
    if test == 1:
        return True
    else:
        return False
    
print(consecutive([1, 6, 9, -3, 4, -78, 0],-3,4))


liste = [1, 6, 9, -3, 4, -78, 0]
def is_con(liste, int1, int2):
    if liste.index(int1) + 1 == liste.index(int2) or liste.index(int1) - 1 == liste.index(int2):
        return True
    return False
print(is_con([1, 6, 9, -3, 4, -78, 0], -78, 4))

def consecutive(list,a,b):
    for x in range(1,len(list)):
        if list[x-1] == a and list[x] == b:
            return True
        elif list[x-1] == b and list[x] == a:
            return True
    return False











