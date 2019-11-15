# Remember that the value of a variable can be updated indefinitely
w = "*"
w = w + "*"
print(w) # what will print(w) display?
w = w + "*"
print(w) # what will print(w) display now?

# We already know the "for" loop. Python also offers another kind of
# loop - 
# loops - how to make a piece of code execute multiple times?
how_many = 10
current_iteration = 0
while current_iteration < how_many:
    print("*")
    # any indendet line of code is part of the loop
    # remember: in python indentations are very important!
    current_iteration = current_iteration + 1
    # there can be as many lines of code in the loop as need
    print("xxx")
print("done")

# exerice 1: using the above code sample write a program
# which will ask the user for a number and print as many astrisks as
# the user demanded


# exerice 2: modify the program from exercise 1 so that it prints a
# triangle from astriks of any height requested by the user
# *
# **
# ***
# ****
# *****
# ...