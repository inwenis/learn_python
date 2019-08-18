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

# Python offers some functions to generate lists
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_2 = list(range(1, 10)) # also a list of numbers from 1 to 9

# why does range(1, 10) needs to be wrapped in a list()?
# list() converts whatever we give to a list.
# the range() function does not return a list. It returns something
# different, that is optimized to work with large values. We will not
# go into details right now but you should not understand