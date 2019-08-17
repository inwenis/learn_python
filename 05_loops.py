# we know we can use variables to compute their sum:
a = 7
b = 8
c = a + b

# but we can also compute how "a + 1" and store it back to a
print("a is now: " + str(a))
a = a + 1
print("a is now: " + str(a))

# multiply c by 2 and store it back to c
print("c is now: " + str(c))
c = c * 2
print("c is now: " + str(c))

# the same works for str variables
hamlet = "To be or "
print(hamlet)
hamlet = hamlet + " to code is the question!"
print(hamlet)

plus = "+"
plus = plus + "+"
# what will print(plus) display?
plus = plus + "+"
# what will print(plus) display?

# -----------------------------------------------
# loops - how to make a piece of code execute multiple times?
how_many = 10
current_iteration = 0
while current_iteration < how_many:
    print("*")
    # any indendet line of code is part of the loop
    # remember: in python indentation is very important!
    current_iteration = current_iteration + 1
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