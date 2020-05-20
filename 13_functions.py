# this script is about functions.
# what are functions?
# we create a function if we have a piece of code which we will be reusing.
# insted of copying-and pasting the same piece of code again and again
# we will create a function and just use our function

# this is a function
# notice that the body of the function must be indented
def create_greeting(name):
    greeting = "hello " + name
    return greeting


message = create_greeting("Bulma")
print(message)
message = create_greeting("Mark")
print(message)

# we called (used) the create_greeting() function with 2 different names.
# the value in paranthesis "Bulma"/"Mark" is passed on to the function.
# so that when the function is executed the "name" variable will hold
# "Bulma" during first execution and "Mark" during the second

# Lets disect the function and name it's parts:
# def - python keyword used to define a funciton
# function name - "create greeting"
# function arguments - "name" - values which can be supplied to our function when it is called
# the indented code is the function "body"
# the "return" statement tells what our function will return

# a function without paramters:
def concatenate_tree():
    tree = ""
    for x in range(1, 5):
        tree = tree + ("*" * x) + "\n"
    return tree

# function without a return statement:
def print_tree():
    for x in range(1, 5):
        print("*" * x)

# function with multiple parameters:
def compute_bmi(weight, height):
    return weight / (height * height)

# functions can also be used to improve the structure/readablity of our code.
# sometimes our code will consist of few steps and we would like to clearly separete them for
# the sake of readablity
# consider this solution to ex. 5.1

def map_to_category(bmi):
    if bmi < 25:
        return "Normal"
    elif 25 <= bmi < 29:
        return "Overweight"
    else:
        return "Obese"

print("input your weight in kg")
weight = float(input())
print("input your height in meters")
height = float(input())
bmi = compute_bmi(weight, height)
category = map_to_category(bmi)
print("your BMI is " + str(bmi) + " category: " + category)

# When writing a funciton you can ask your self "should my function return a value or direclty print it?"
# As a general rule of thumb you can assume that it's preffered to have function returning values.
# There are few reasons for this:
#  - makes automated unit testing easier/possible
#  - function is more reusable (sombody using your function might want to modify the returned value before printing it)

# function names - same rules as variables

# we have already use a lot of funcitons created by authors of the python language
# print()/int()/input()/... -> all of them are functions.

# passing values by value/ref
def foo(x):
    x[1] = 10

def bar(x):
    x = [1,2,3]

l = [10, 9, 8]
print(l)
foo(l)
print(l)
bar(l)
print(l)

# why did foo() modify our list, but bar() did not?
# when we call foo() and bar() "x" is just another name for a list called "l".
# because "x" is pointing to the same exact list in memery as "l" modyfying x[5]
# changes the lists value.
# But in bar we actually create a new list and point x to it.
# hence in bar() we have 2 lists in memory, x and l. Althogh x initially points to the same list as l, we
# create a new list and point x to it.

# Memory during foo()
# |----------|
# |-[10,9,8]-| <-l   <-x
# |----------|
# |----------|
# |----------|

# Memory when foo() finishes
# |----------|
# |-[10,10,8]| <-l
# |----------|
# |----------|
# |----------|

# Memory when bar() is executing
# |----------|
# |-[10,10,8]| <-l
# |----------|
# |-[1,2,3]--| <-x
# |----------|

# Memory when bar() is finishes
# |----------|
# |-[10,10,8]| <-l
# |----------|
# |----------|
# |----------|

# functions can call other functions

def create_very_greeting(name):
    regular_greeting = create_greeting(names)
    very_greeting = "very " + regular_greeting
    return regular_greeting

create_very_greeting("Mark")

# exercises
# wirte a function which will accept a list and int and check if the int is in the list
# should be used like:
# c = contains([1,2,3,4], 5)
# should return True/False

# ex2
# create a function 
TODO need more here
