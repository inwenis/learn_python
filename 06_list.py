# lists in python allow us to store many values in a single variable
fruits = ["apple", "carrot", "banana"]
primes = [2, 3, 5, 7, 11, 13, 17]

# to access a specific element from a list we need to know it's
# index. The index of a element is it's posistion in the list. Index
# of the first element is 0, index of the second element is 1...
print(fruits[0]) # will print "apple"
print(fruits[1]) # will print "carrot"
b = fruits[2]
print(b) # will print "banana"

# Lists are very usefull because we can execute the same code for
# every elemnt in a list. To do this we use the "for" loop.
for fruit in fruits:
    print(fruit)
# The print statement will be executed once for every item in the
# fruits list. Python will assing subsequent values form "fruits" to
# the "fruit" variable.

# loop over primes list
for x in primes:
    print(str(x) + " is a prime number")
    # we can have multiple statements under a for
    # untill they are indented they will be executed as part of the
    # loop
    print("The square of " + str(x) + " is " + str(x*x) )
    x_cubed = x*x*x
    print("The cube of " + str(x) + " is " + str(x_cubed) )

# Python offers some functions to generate lists
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_2 = list(range(1, 10)) # also a list of numbers from 1 to 9

# Why does range(1, 10) needs to be wrapped in a list()?
# list() tries to convert whatever we give to a list. The range()
# function does not return a list. It returns something different,
# that is optimized to work with large ranges. We will not go into
# details right now but you should understand that list() just like
# int(), str(), float() converts something to a list.

for x in numbers_2:
    print(x)

# Just like with an if/elif/else you can put any code under a "for"
# loop. You can nest also loops in loops

# print power table (table of multiplied numbers)
for x in numbers:
    for y in numbers:
        print(str(x) + "*" + str(y) + "=" + str(x*y) + " ", end="")
        # notice that since the above print is indented twice it's
        # part of the inner loop. The inner loop will be executed
        # for every x in "numbers".
        # print(..., end="") tell python to display some text to the
        # console but does not move the cursor to next line
    print() # an empty print() moves the cursor to next line

# nest if under a for loop
for x in numbers:
    if x % 2 == 0: # the % sign means the modulo operation*
        print(str(x) + " is even")

# The module operation return the reminder after division. Examples:
# 9 % 5 = 4
# 7 % 2 = 1
# 4 % 2 = 0

# Of course in loops you can use varaibles defined before the loop:
# Sum all even numbers
sum = 0
for x in numbers:
    if x % 2 == 0:
        sum = sum + x
print("sum of all even ints from " + str(numbers) + " = "+ str(sum))

# Find smallest number in a list
min = 0
for x in [1, 100, 2, 5, 3, -5, 9, -1, 2, -17]:
    if x < min:
        min = x
print("min = " + str(min))

# exericse 1: Create a list with names of months and display all of
# them.

# exercise 1: Display all odd numbers from 1 to 50.


# exercise 2: Sum all numbers in range 1 to 100.


# exercise 3: Create a list filled with random numbers. Find the
# largest nmber in that list.


# exercise 4: Display a rectangle from * with width and height
# specified by the user. Example:
# please provide width:
# 7
# please privide height:
# 3
# *******
# *******
# *******


# exercise 5: Check if a number provided by the user is prime. A
# prime number is number which can only be divided without a reminder
# only by itself or 1. Examples of prime numbers: 2, 3, 5, ..., 79.

# Hot to check if a number x is prime?
# One solution is to loop over numbers from 2 to x-1 and check if x
# can be divided without a reminder by any of them.
