# Exercise 1 - Odd or even
Write a program which asks the user for a numer and test if the
number is odd or even. The program should output a message as shown
below.
```
> 5
> Number 5 is odd
```
```
> 24
> Number 24 is even
```
Hint: the [modulo](https://en.wikipedia.org/wiki/Modulo_operation)
operation will be useful for this exercise. Python uses the `%` sign
for modulo operaiton.

# Exercise 2 - Napoleon is history
Write a program which will ask the user for his/hers birth date and
print out when the user "turned"/"will turn" 18, 30, 50, 100 years
old.

### Ad 1
Extend your program to also print how many years after the end of
Napoleon wars the user was born.

Did you know that the oldest man, Gustav Gerneth, born in 1906,
was born closer to Napoleon wars than to the year 2019?

### Ad 2.
Rewrite your program using as few LOC (lines of code) as possible.

### Ad 3.
Rewrite your program using as few characters as possible.

# Exerice 3 - Calculator
Write a simple calculator. The program should ask the user for two
numbers and what operation to perform: +, -, *, / , %.
Perform the operation on supplied numers and display the resut.

Example:

```
> 21[enter]
> 12[enter]
> /[enter]
> 1.75
```

# Exercise 4 - Compound interest
Write a program which will compute the interest for a bank deposit.
The program should ask the user for:
- deposit sum
- annual interest rate for the deposit
- period of deposit in number of months

The interest rate is capitalized only once at the end of the deposit.

Example:
```
> 1000[enter]
> 20[enter]
> 6[enter]
> Deposit: 1000
> Interest rate: 20%
> Period of deposit: 6 months
> Interest: 100
> Ttotal account after 6 months: 1100
```

### Ad 1.
Extend the program to compute deposit interest taxes and deduct them
from the interest.
```
> 1000[enter]
> 20[enter]
> 19[enter]
> 6[enter]
> Deposit: 1000
> Interest rate: 20%
> Taxes: 19%
> Period of deposit: 6 months
> Interest: 81
> Ttotal account after 6 months: 1081
```