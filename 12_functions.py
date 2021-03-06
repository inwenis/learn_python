# What are functions?

# Often we will think "if only I could reuse this piece of code with
# different values". As an example lets consider this code creating
# greeting messages:

names = ["Mark", "Johny", "Lisa"]
hour_now = 16

if hour_now < 12:
    message1 = "Good morning " + names[0]
else:
    message1 = "Good afternoon " + names[0]

if hour_now < 12:
    message2 = "Good morning " + names[1]
else:
    message2 = "Good afternoon " + names[1]

if hour_now < 12:
    message3 = "Good morning " + names[2]
else:
    message3 = "Good afternoon " + names[2]

print(message1)
print(message2)
print(message3)

# With a function we can extract the code creating the greeting
# message. This is how such a function would look like:
# (we will disect the function in a moment)

def create_greeting(name, hour):
    if hour < 12:
        message = "Good morning " + name
    else:
        message = "Good afternoon " + name
    return message

# We can now rewrite our code using the function:
message1 = create_greeting(names[0], hour_now)
message2 = create_greeting(names[1], hour_now)
message3 = create_greeting(names[2], hour_now)

print(message1)
print(message2)
print(message3)

# In lines 41-43 you see our create_greeting() function being invoked
# 3 times. Each time we pass a different name to it and the same
# hour. Every time we invoke create_greeting() python will:
# - jump to line 33
# - execute the function's code (it is indented)
# - jump back to the place from which the function was called
# - use the creted message as the value returned by the function
#   ('return message' statement)

message1 = create_greeting(names[0], hour_now)
#                         ____________________
# When invoking a function we give it values by putting them in
# paranthesis and separating them by comas (as underlined above). The
# invocation of create_greeting() in L58 will set name=names[0] and
# hour=hour_now.

# We can use our function also in a loop:
for n in names:
    msg = create_greeting(n, hour_now)
    print(msg)

# Function do not have to acctept input parameters
def concatenate_tree():
    tree = ""
    for x in range(1, 5):
        tree = tree + ("*" * x) + "\n"
    return tree

t = concatenate_tree()
print(t)

# Function do not have to return any value
def concatenate_and_print_tree():
    tree = ""
    for x in range(1, 5):
        tree = tree + ("*" * x) + "\n"
    print(tree)

concatenate_and_print_tree()

# Another function with 2 parameters
def compute_bmi(weight, height):
    return weight / (height * height)

# Function with a single input argument
def simple_greeting(name):
    return "Welcome " + name

# Lets disect the simple_greeting() function and name its parts:
#  - def - python keyword used to tell python "hey, we're defining a
#    function"
#  - function name - "simple_greeting"
#  - function arguments - "name" - values which we need to supply
#    when calling the function
#  - function body/code - indented code is the function "body"
#    python will treat unindented code as regular code, not part of
#    the function
#  - return - python keyword used to tell "my function returns this
#    value"

# Function names follow the same rules as variable names:
#  - must start with a letter or _ character
#  - can not contain spaces
#  - by convention words are separated by _
#  - by convention letters are lower case

# exercise 1: complete the find_min() function so that it finds the
# smallest value in a list

def find_min(values):
    # TODO - complete the function - find the minimum value in list
    # `values`.
    # remeber that function's bodies must be indented
    return 0 # once you find the minimal value return it here insted of returning a 0

nums = [99, 17, 10, 2, 45, 7, 12, 10]
print("smallest number is " + str(find_min(nums)))

# exercise 2: from scratch write a function which accepts two int
# parameters a and b, and returns a^b (a to the power of b).
# hint: you will need: a `for` loop, `range()`, and multiplication.


# Functions can also be used to improve the structure and readablity
# of our code (even if they are used only once). Sometimes our code
# will consist of few steps and we would like to clearly separete
# them for the sake of readablity.

# Consider this solution to exercise 5.1. Because we can define
# functions for "computing BMI" and "mapping BMI to a category" code
# from line 149 is quite self explanatory.

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

# When writing a funciton you can ask your self "should my function
# return a value or print it immediately?". As a general rule of
# thumb assume that it's preffered for functions to return values.
# There are at least 2 reasons:
#  - makes automated unit testing easier/possible (unit testing is
#    not convered by these introductory scripts)
#  - functions are more reusable (sombody using your function might
#    want to modify the returned value before printing it)
# This is why map_to_category() only returns the category name and
# does not print it.

# Althought we just now started writing functions, we have already
# used them a lot. So far we used funciton written by the authors of
# python.
# print()/int()/input()/... - all are functions.

# exercise 3: wirte fibonacci(n) funciton which accepts an integer n
# and returns the n-th Fibonacci number.


# exercise 4: create a function which given a list of users will
# generate the "Liked by" facebook message.
# If a post is liked by a single person X just return "Liked by X".
# If a post is liked by 2 people return "Liked by X and Y"
# If a post is liked by 3 people return "Liked by X, Y and 1 other"
# If a post is liked by 4+ people return "Liked by X, Y and Z others"
# Test your function using lists of different lengths
