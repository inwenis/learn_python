# Previously we have created variables and assigned different values
# to them. Both text and numbers.
x = 42
y = "Hello World"

# Python distinguishes types of values.
# Variable x stores an integer. An integer is a whole number without
# fractions. The name "integer" is often abbreviated as "int"
# Variable y stores a string variable. A string is text. The name
# "string" is often abbreviated as "str"

# Other types in Python are:

# this is a float, a fractional number
euro_to_dkk = 7.47
height = 160.5

# this is a boolean variable, it can only store True or False. Often
# abbreviated as "bool"
batch_processing = True
order_payed = False

# We can easily do operations on:
# - int and int
# - int and float
# - str and str
a = x + 50
price_in_dkk = 12 * euro_to_dkk  # this is multiplication
dkk_to_euro = 1 / euro_to_dkk

hamlet_beg = "To be or "
hamlet_all = hamlet_beg + " to code is the question!"

# We can not add int to str. If you uncomment the line below Python
# will complain that it does not know how to add a int and str.
# d = 40 + "text"

# For this reason we can not have a print statement like below
# print("the value of x is " + x)
# if you uncomment it python will complain "can not add str to int"


# How to convert one type to another?

# Sometimes we will have text containing numbers and would like to
# add it like an int.
# Sometimes we want to display value of a int variable like in
# line 39.

# For this purpose Python offers function converting values to other
# types

# str() to convert anything (int/float/bool) to str
g_constant = 9.8
print("the value of variable g_constant is " + str(g_constant))

# we could also do it as:
g_constant_as_text = str(g_constant)
print("the value of g_constant is " + g_constant_as_text)

# str() for bool
love_for_python = True
print("Already love python? My love is " + str(love_for_python))

# int() and float() to convert from something to int or float
h = "123"
k = int(h) + 20
print("Value of k: " + str(k))

p = "3.14"
p_double = float(p) * 2
print("Value of p_double: " + str(p_double))

# Note that since you can pass any text to int() and float() it is
# possible that we accidentally pass some inconvertible text to
# int() or float(). If this happens python will "throw an exception",
# display an error message and stop execution.

# exercise 1: uncomment the following lines, execute code and see
# what happens
# v_desc = "your speed is 50 km/h"
# v = int(v_desc)
# Does the error message written by python make any sense to you?


# exercise 2: create variables of all types you know so far.
# Display values of all variables in a print() with prepended text.
# Example:
tz_age = 22
print("value of tz_age is " + str(tz_age))


# exercise 3: create variables of different types and use conversion
# functions to convert:
# - str to int
# - int to str
# - bool to str
# - str to float
# - float to str
# - int to float
# - float to int, notice what happens to the fractional part of
#   floats during conversion to int


# exercise 4: deliberately try to add str to int, float to str, and
# see what happens when you execute the script. The error message
# should tell you in which line of code python encountered an issue.
# There should also be a description of the error. Being able to read
# error messages is very helpful.
