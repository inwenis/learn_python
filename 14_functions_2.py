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
# The ascii art below tries to explain what happend in the memory
# during execution of lines L6-L17

# Memory in L13
# |---------|
# |-[1,2,3]-| <-l
# |---------|
# |---------|

# Memory just before L7 is executed
# |---------|
# |-[1,2,3]-| <-l   <-x
# |---------|
# |---------|

# Memory after L7 is executed
# |---------|
# |-[1,9,3]-| <-l   <-x
# |---------|
# |---------|

# Memory in L15
# |---------|
# |-[1,9,3]-| <-l
# |---------|
# |---------|

# Memory just before L10 is executed
# |---------|
# |-[1,9,3]-| <-l   <-x
# |---------|
# |---------|

# Memory after L10 is executed
# |---------|
# |-[1,9,3]-| <-l
# |-[1,2,3]-| <-x
# |---------|
# |---------|

# Memory in L17
# |---------|
# |-[1,9,3]-| <-l
# |---------| (the list is forgotten once we exit bar())
# |---------|

# exercise 1: write a function replace_odd(lst) which will replace
# all numbers on odd indexes with a 0 in a list.

# replace_odd([1, 2, 10, 15, 100, 1, 2, 3])
# expected result: [1, 0, 10, 0, 100, 0, 2, 0]

# tip: how to loop over a list using the lists indexes?
lst = [1, 2, 10, 15, 100, 1, 2, 3]
length_of_lst = len(lst)
for i in range(0, length_of_lst):
    print(lst[i])

# Solution
def replace_odd(lst):
    for i in range(0, len(lst)):
        if i % 2 == 1:
            lst[i] = 0
    return lst
replaced = replace_odd([1, 2, 10, 15, 100, 1, 2, 3])
print(replaced)


# Functions can call other functions:

def create_greeting(name):
    return "Good morning " + name

def create_very_greeting(name):
    regular_greeting = create_greeting(name)
    very_greeting = "very " + regular_greeting
    return regular_greeting

very_greeting = create_very_greeting("Mark")
print(very_greeting)

# exercises 2: wirte a function which will accept a list and a number
# and check if the number is in the list.

# example:
# c = contains([1,2,3,4], 5) # should return False


# exericse 3: write a function which creates a list with Fibonacci
# numbers.

# example:
# f = generate_fibbo(7)
# print(f) # should print [0, 1, 1, 2, 3, 5, 8]

# tip: how to create a list and append values to it?
lst = [] # this is an empty list
lst.append(1)
lst.append(2)
print(lst)

# the same can be achieved using list addition
lst = [] # this is an empty list
lst = lst + [1]
lst = lst + [2]
lst = lst + [3, 4]
print(lst)
