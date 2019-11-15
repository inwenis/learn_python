# Because lists are a very important data type we will learn more
# about what we can do with lists

# We already know how to access items in a list by using their
# indexes
fruits = ["apple", "carrot", "banana"]
print(fruits[1]) # will print "carrot" since indexes starts at 0

# Sometimes we might need to access items from the end insted of from
# the beginning like we do with indexes.
# Lists in Python support "negative indexing" allowing us to access
# items from the end
print(fruits[-1]) # index -1 refers to the last item
print(fruits[-2]) # index -2 refers to the second last item, etc...

# Slicing lists is also very useful if we need to extract a sublist.
# We do this by specyfying from/to indexes
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits_sub_list = fruits[2:5]
print(fruits_sub_list)

# Using slicing we can also get a sublist from the tail using
# negative indexing
print(fruits[-5:-1]) # notice that here "mango" will not be printed

# In case of slicing from the end -1 means the second last element
# hence above we will not get "mango". If we need a sublist including
# the last element, this is how we do it
print(fruits[-5:])

# To get first the first 5 elements of a list we can do either:
print(fruits[:5])
print(fruits[0:5])

# We can even create a slice of a list containing the whole list.
# Later we will find out why this is useful
print(fruits[:]) # by not specifying from/to we get the whole list

# Can we ask python to return a slice of a list, but only every
# second element? We can:
numbers = list(range(0, 10))
even_from_first_5 = numbers[1:5:2]
print(even_from_first_5)
# numbers[1:5:2] - explanation:
#         | | |
#         start from the second item which is "2" (numbers[0] is "1")
#           | |
#           take elements untill index 5 exclusive (aka. 4 inclusive)
#             |
#             take every 2nd (second) item
# The same way we can ask for every 3rd, 4th, ... item.
# The numbers used for slicing are usually named: [from:to:step]

# To get every second item from the whole list:
print(numbers[::2])

# We can even ask for items from the end setting step to -1
print(numbers[::-1]) # reversed list
print(numbers[::-2]) # every second item of a reversed list

# Reversing lists is very useful because often we will need to
# process a list from the end.

things_to_do = ["hover", "iron", "dishes", "walk", "read book", "code"]

print("wrong order of doing things:")
for x in things_to_do:
    print(x)

print("correct order of doing things:")
for x in things_to_do[::-1]:
    print(x)

# Slicing lists might be confusing because of the many possibilities
# it gives us: from/to/setpping/backwards/forwards. Don't worry if
# you will need to comeback the the interactive shell again and agin
# to remind your self how slicing works. I do it too all the time.

# exercise 1: create a list with months.
# a) print it forwards
# b) print it backwards
# c) print sublist of winter months
# d) print sublist of summer months reversed
# e) print months of II and III quater
# f) print odd months
# g) print even months from march to october


# exercise 2: A coder's work is mostly reading existing code. Read
# the commented code below and before running it, try to deduce what
# will be the output of the code. Write it down, run the code, how
# many list slices did you predict correctly?

languages = ["C#", "Java", "Python", "JavaScript", "C", "C++", "Ruby"]
# print(languages[0:2])
# print(languages[:])
# print(languages[:4])
# print(languages[-1:])
# print(languages[-5:])
# print(languages[::2])
# print(languages[::-1])
# print(languages[::-3])

# exercise 3: Write a program which will ask the user for a number N.
# Then the program will compute the sum of all even numbers from
# 0 to N.


# exercise 4: Create a list with random numbers. Print only numbers
# greater than 10.


# exercise 5: Write a program which will ask the user for a number N
# and print numbers from 1, 2, 3, 4,... untill their sum exceeds N
