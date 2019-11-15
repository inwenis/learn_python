# When you write code like below you create a variable.
x = 123
# We have created a variable called "x" and assigned it the value
# 123. python will on our behalf reserve some memory and store the
# value 123 in it.

# Whenever we would like to access this value we need to use the
# variable name "x".
print(x)
# Important!
# Notice that print("x") means something different than print(x)
# The former tells python to display the text "x", where as the
# latter tells python to display the value of varaible x.

# We can create as many variables as we need.
my_age = 42
birth_year = 1980
a = 999
# Variable names can not contain spaces.
# Name of a variable should hint what it will be used for.
pi = 3.14
current_season = "November"
welcome_message = "Welcome to our homepage"

# this is a bad name
three = 3
# this is much better
max_cards_per_user = 3

# variables can be used in many ways
current_year = birth_year + my_age
print(current_year)

print(welcome_message + " in " + current_season)

# exercise 1: create two variables, assign some big numbers to them
# and print their sum, difference, product (multiplication),
# quotient (division)


# exercise 2: create two variables, assgin some text to them and
# display the concatenated text.