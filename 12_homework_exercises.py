# Exercise 1 - Sum of 3s and 5s
# Write a program which given the number N will sum all numbers
# dividable by 3 and 5 which are less or equal to N.
# N=10
# 1 2 3 4 5 6 7 8 9 10
# 3 + 5 + 6 + 9 + 10 = 33

# Solution
# n = input("Provide n > ")  # commented for easier testing
n = 10
s = 0
for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0:
        s += i

print("Exercise 1 -------------------------------------------------")
print("sum of multiples of 3 and 5 lower than " + str(n) + " is "+ str(s))

# Exercise 2 - Factorial
# Write a program which will compute n factorial.
# n factorial denoted as n! is the product of all numbers less than
# or equal to n.
# 3! = 3 * 2 * 1 = 6
# 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 = 5040

# Solution
def factorial(n):
    if n == 0:
        return 1
    else:
        s = 1
        for i in range(1, n+1):
            s *= i
        return s

print("Exercise 2 -------------------------------------------------")
print("factorial(0) = " + str(factorial(0)))
print("factorial(1) = " + str(factorial(1)))
print("factorial(2) = " + str(factorial(2)))
print("factorial(3) = " + str(factorial(3)))
print("factorial(4) = " + str(factorial(4)))
print("factorial(10) = " + str(factorial(10)))

# Exercise 3 - Reversed
# Write a program which will reverse text inputted by the user.
# input:  "coding in python is fun"
# output: "nuf si nohtyp ni gnidoc"

# Solution
# text = input("Provide some text to be reversed > ")  # commented for easier testing
text =  "coding in python is fun"
print("Exercise 3 -------------------------------------------------")
print(text[::-1])

# tip: strings are just lists of characters
# Complete the exercise:
# a) using slicing
# b) without slicing

# Solution without slicing
reversed_text = ""
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]
print(reversed_text)

# Exercise 4 - Square
# Write a program which will print a square from asterisks.
#    ***
#    * *
#    ***

# Solution
print("Exercise 4 -------------------------------------------------")
print("***")
print("* *")
print("***")

# Ad 1.
# Modify the program so that the user can specify the side length.
w = 5
h = 4
square = ""
square += "*" * w + "\n"
for i in range(0, h-2):
    for i in range(0, w):
        if i == 0 or i == w-1:
            square += "*"
        else:
            square += " "
    square += "\n"
square += "*" * w

print(square)

# more compact solution:
square = ""
square += "*" * w + "\n"
for i in range(0, h-2):
    square += "*" + " " * (w - 2) + "*\n"
square += "*" * w

print(square)

# Exercise 5 - Fibonacci
# Write a program which will print out n elements of the fibonacci
# sequence.
# input: 6
# output:
# 1
# 1
# 2
# 3
# 5
# 8

# Solution
def fibonacci(n):
    a = 0
    b = 1
    for i in range(1, n):
        b_old = b
        b = b + a
        a = b_old
    return b

print("Exercise 5 -------------------------------------------------")
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(10))

# Ad 1.
# For each printed fibonacci number also print out the ratio of the
# current to the previous number.

for i in range(1, 30):
    fib_prev = fibonacci(i-1)
    fib_i = fibonacci(i)
    print("fib(" + str(i) +") = " + str(fib_i) + "ratio=" + str(fib_i/fib_prev) )

# Exercise 6: Intersection
# Create two lists of numbers. Write a programs which will print
# numbers:
# a) present in both lists
# a) present only in first list


# Exercise 7: Fizz Buzz
# Write a program that prints the numbers from 1 to 100. For
# multiples of three print "Fizz" instead of the number and for
# multiples of five print "Buzz". For numbers which are multiples of
# both three and five print "FizzBuzz".
