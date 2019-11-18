# Remember that the value of a variable can be updated indefinitely
i = 0
i = i + 1
print(i) # what will print(i) display?
i = i + 1
print(i) # what will print(i) display now?

# We already know the "for" loop. Python also offers the "while"
# loop

how_many = 10
current_iteration = 0
while current_iteration < how_many:
    print("value of current_iteration is now: " + str(current_iteration))
    print("*")
    # any indented line of code is part of the loop
    # remember: in python indentations are very important!
    current_iteration = current_iteration + 1
    # there can be as many lines of code in the loop as need
    print("xxx")
print("done")

# Loop with a accumulator variable:
accumulator_variable = "text"
i = 0
while i < 5:
    print(accumulator_variable)
    accumulator_variable = accumulator_variable + " more text"
    i = i + 1
print("done")

# exercise 1: using the above code sample write a program
# which will ask the user for a number and print as many asterisks as
# the user requested.


# exercise 2: modify the program from exercise 1 so that it prints a
# triangle from asterisks of any height requested by the user.
# *
# **
# ***
# ****
# *****
# ...


# How to use a "while" loop with lists?
# Python offers the len() function which can return the length of a
# list. Knowing the length of a list we can loop over with a "while"
# loop

letters = ["a", "b", "c", "d", "e", "f"]
length = len(letters)
print(length)

i = 0
while i < length:
    print(letters[i])
    i = i + 1

# A variable named "i" is often used with loops. "i" stands for
# "index". The advantage of "for" loops is that we don't have to
# manage an "index" variable.

# exercise 3: what will be the output of the commented code below?
# First try to predict the outcome and then run the code.

#grades = [4.2, 3.7, 5.2, 2.5]
#length = len(grades)
#i = 0
#while i < grades:
#    print(grades[i])


# exercise 4: rewrite exercise 1 & exercise 2 from 07_list.py using
# "while" loops.
# Which version of the code do you consider more readable?
