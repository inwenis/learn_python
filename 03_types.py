# Previously we have created variables and assigned different values
# to them. Both text values and numbers.
x = 42
y = "Hello World"

# Python distinguishes types of values.
# Variable x stores an integer. An integer is a whole number without
# fractions. The name "integer" is often abbrevianted as "int"
# Variable y stores a string variable. A string is text. The name
# "string" is often abbreviated as "str"

# Other types in Python are:

# this is a float, a fractional number
g = 4.2
z = 12.001

# this is a boolean variable, it can only store True or False. Often
# abbreviated as "bool"
u = True
j = False

# We can easily do operations on:
# - int and int
# - int and float
# - str and str
f = 60
a = x + 50
b = x * x # this is multiplication
c = 20 / x

i = 4.2
j = 91.001
d = i + j

hamlet_beg = "To be or "
hamlet_all = hamlet_beg + " to code is the question!"

# But we can not add int to str. If you uncomment the line below
# Python will complaing that it does not know how to add a int and
# str.
# d = x + hamlet_beg

# For this reason we can not have a print statement like below
# print("the value of x is " + x)
# if you uncomment it python will complaing "can not add str to int"


# How to convert one type to another?

# Sometimes we will have text containing numbers and would like to
# add it like a int. Sometimes we want to display value of a int
# variable like in line 45.

# For this purpose Python offers function converting values to other
# types

# str() to convert anything (int/float/bool) to str
g = 42
# print("the value of g is " + g) # this will not work
print("the value of g is " + str(g)) # this will work

# we could also do it as:
g = 42
g_as_text = str(g)
print("the value of g is " + g_as_text)

# str() for float
g_constant = 9.8
print("the value of variable g_constant is " + str(g_constant))

# str() for bool
love_for_python = True
print("the value of variable g_constant is " + str(love_for_python))

# int() and float() to convert from something to int or float
h = "123"
k = int(h) + 20
print("Value of k: " + str(k))

p = "3.14"
p_double = float(p) * 2
print("Value of p_double: " + str(p_double))

# Note that since you can pass any text to int() and float() it is
# possible that we accidentally will pass some unconverable text to
# int() or float(). If this happens python will "throw an excetpion",
# display an error message and stop execution.

# uncomment the following lines to see what happens
# v_desc = "your speed is 50 km/h"
# v = int(v_desc)

# exercise 1: create variables of all types you have learned so far.
# Display values of all variables in a print() with some preceeding
# text message.
# Example:
tz_age = 22
print("value of tz_age is " + str(tz_age))

# exercise 2: create as many different variables as you need and
# use conversion functions to convert:
# - str to int
# - int to str
# - bool to str
# - str to float
# - float to str
# - int to float
# - float to int, notice what hapens to the fractional part of a
#   float when it's converted to int


# exercise 3: deliberetely try to add str to int, float to str, and
# see what happens when you execute the script. The error message
# should tell you in which line of code python encountered an issue.
# There should also be a description of the error. Being able to read
# error messages is very helpful.
# Deliberetely try to convert unconvertable strings to int and float
# to see error messages.
