# in Python variables have different types
# the most common types are:
# int - integer (numbers like 1, 2, 100, 5, 0, -1, -20)
# str - string, text ("this", "or", "just any text")
# float - fractional numer (3.14, 20.0, 21.154)
# list - a list stores multiple variabes (we'll cover this later)

# to ask Python for a type of a variable we use... type()

# TODO - this asks for type of value not variable
print(type(123))
print(type(12.3))
print(type("hello"))
print(type("123"))

x = 99
print(type(x))

# some types can be converted between each other
# almost any type can be converted to a string using str()
# some strings can be converted to a int using int()
# some strings can be converted to a float using float()

a = "123"
b = int(a)
print("variable a is of type:")
print(type(a))
print("variable b is of type:")
print(type(b))

# exercise 1: create variables of different types and display their
# types and values


# exercise 2: since you know how to convert text to numbers:
# go back to 03_input.py and fix exercise 2 so that numbers are
# actually added
