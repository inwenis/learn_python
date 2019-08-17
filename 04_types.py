# in Python variables have different types
# the most common types are:
# int - integer (numbers like 1, 2, 100, 5, 0, -1, -20)
# str - string, text ("this", "or", "just any text")
# float - fractional numer (3.14, 20.0, 21.154)
# list - a list storing multiple variabes (we'll cover this later)

# to ask Python for a type of a variable we use... type()

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

some_text = "123"
number = int(some_text)
print("some_text is of type:")
print(type(some_text))
print("number is of type:")
print(type(number))

# exercise 1: create variables of different types and display their types and vlaues


# exercise 2: since you know how to convert text to numbers:
# go back to 03_input and fix exercise 2 so that number are actually added
