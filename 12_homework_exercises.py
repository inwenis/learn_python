# Exercise 1 - Sum of 3s and 5s
# Write a program which given the number N will sum all numbers
# dividable by 3 and 5 which are less or equal to N.
# N=10
# 1 2 3 4 5 6 7 8 9 10
# 3 + 5 + 6 + 9 + 10 = 33

# Solution
# n = input("Provide n > ")  # commented out for easier testing
n = 10
s = 0
for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0:
        s += i
print(s)

# Exercise 2 - Factorial
# Write a program which will compute n factorial.
# n factorial denoted as n! is the product of all numbers less than
# or equal to n.
# 3! = 3 * 2 * 1 = 6
# 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 = 5040

# Exercise 3 - Reversed
# Write a program which will reverse text inputted by the user.
# input:  "coding in python is fun"
# output: "nuf si nohtyp ni gnidoc"

# tip: strings are just lists of characters
# Complete the exercise:
# a) using slicing
# b) without slicing

# Exercise 4 - Square
# Write a program which will print a square from asterisks.
#    ***
#    * *
#    ***

# Ad 1.
# Modify the program so that the user can specify the side length.

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

# Ad 1.
# For each printed fibonacci number also print out the ratio of the
# current to the previous number.

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
