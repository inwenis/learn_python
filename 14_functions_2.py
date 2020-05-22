# This script continues the topic of functions - passing values by
# reference.

# Run the following code and closely inspect the output.

def foo(x):
    x[1] = 9

def bar(x):
    x = [1,2,3]

l = [1, 2, 3]
print(l)
foo(l)
print(l)
bar(l)
print(l)

# Why did foo() modify our list "l", but bar() did not?

# When we call foo() and bar() "x" is just another name for a list
# called "l". Because "x" is pointing to the same exact list in
# memory as "l" modyfying x[1] changes the value in the list.
# But in bar() we actually create a new list and point x to it. Hence
# in bar() we have 2 lists in memory, x and l. Althogh x initially
# points to the same list as l, we create a new list and point x to
# it in L10.

# Memory in L13
# |---------|
# |-[1,2,3]-| <-l
# |---------|
# |---------|

# Memory during foo() execution
# |---------|
# |-[1,9,3]-| <-l   <-x
# |---------|
# |---------|

# Memory in L15
# |---------|
# |-[1,9,3]-| <-l
# |---------|
# |---------|

# Memory during bar() execution
# |---------|
# |-[1,9,3]-| <-l
# |---------|
# |-[1,2,3]-| <-x
# |---------|

# Memory in L17
# |---------|
# |-[1,9,3]-| <-l
# |---------|
# |---------|

# TODO filip - exercise here

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
