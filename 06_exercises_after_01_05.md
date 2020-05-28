# Exercise 1 - Odd or even
Write a program which asks the user for a number and test if the
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
for modulo operation.

## Solution

```Python
print("Please type in a number which will be tested for parity")
text_input = input()
x = int(text_input)
if x % 2 == 0:
    print("Number " + str(x) + " is even")
else:
    print("Number " + str(x) + " is odd")
```

# Exercise 2 - Napoleon is history
Write a program which will ask the user for his/hers birth year and
print out when the user "turned"/"will turn" 18, 30, 50, 100 years
old.

## Soluiton

```Python
print("Please type in your birth year")
text_input = input()
x = int(text_input)
_18_birthdate = x + 18
_30_birthdate = x + 30
_50_birthdate = x + 50
_100_birthdate = x + 100
print("You will turn 18 in " + str(_18_birthdate))
print("You will turn 30 in " + str(_30_birthdate))
print("You will turn 50 in " + str(_50_birthdate))
print("You will turn 100 in " + str(_100_birthdate))
```

### Ad 1.
Extend your program to also print how many years after the end of
Napoleon wars the user was born.

Did you know that the oldest man, Gustav Gerneth, born in 1906,
was born closer to Napoleon wars than to the year 2019?

## Solution
```Python
print("Please type in your birth year")
text_input = input()
x = int(text_input)
_18_birthdate = x + 18
_30_birthdate = x + 30
_50_birthdate = x + 50
_100_birthdate = x + 100
end_of_napoleon_wars = 1815
diff = x - end_of_napoleon_wars
print("You will turn 18 in " + str(_18_birthdate))
print("You will turn 30 in " + str(_30_birthdate))
print("You will turn 50 in " + str(_50_birthdate))
print("You will turn 100 in " + str(_100_birthdate))
print("You were born " + str(diff) + " years after end of Napoleon wars")
```

### Ad 2.
Rewrite your program using as few LOC (lines of code) as possible.

## Solution
```Python
x = int(input("Please type in your birth year"))
print("You will turn 18 in " + str(x + 18))
print("You will turn 30 in " + str(x + 30))
print("You will turn 50 in " + str(x + 50))
print("You will turn 100 in " + str(x + 100))
print("You were born " + str(x - 1815) + " years after end of Napoleon wars") # Napoleon wars ended in 1815
```
### Ad 3.
Rewrite your program using as few characters as possible.

## Solution
```Python
# I kept redundant spaces so the program remains comprehensible
a = "You will turn "
b = " in "
n = "\n"
x = int(input("Please type in your birth year"))
o = a + "18"  + b + str(x+18)   + n +\
    a + "30"  + b + str(x+30)   + n +\
    a + "50"  + b + str(x+50)   + n +\
    a + "100" + b + str(x+100)  + n +\
"You were born "  + str(x-1815) + " years after end of Napoleon wars"
print(o)
```

## Solution 2
Using python featuer not yet covered by these intro scripts we can
shorten our code even further
```Python
a, b, x = "You will turn ", " in ", int(input("Please type in your birth year"))
o = f"{a}18{b}{x+18}\n{a}30{b}{x+30}\n{a}50{b}{x+50}\n{a}100{b}{x+100}\nYou were born {x-1815} years after end of Napoleon wars"
print(o)
```

# Exercise 3 - Calculator
Write a simple calculator. The program should ask the user for two
numbers and what operation to perform: +, -, *, / , %.
Perform the operation on supplied numbers and display the result.

Example:

```
> 21[enter]
> 12[enter]
> /[enter]
> 1.75
```

## Solution
```Python
a = int(input("Number A:"))
b = int(input("Number B:"))
print("Select operation + - / * %")
operator = input()
if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "/":
    result = a / b
elif operator == "*":
    result = a * b
elif operator == "%":
    result = a % b
else:
    print("operator '" + operator + "' is unsupported")
print(result)
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
> Total account after 6 months: 1100
```

## Solution
```Python
deposit_sum =    int(input("deposit sum:"))
interest_rate =  float(input("interest rate in %:"))
months =         int(input("nuber of months:"))

interest = deposit_sum * (interest_rate/100) * (months/12)
total_account = deposit_sum + interest

print("Deposit: " + str(deposit_sum))
print("Interest rate: " + str(interest_rate) + "%")
print("Period of deposit: " + str(interest_rate) + " months")
print("Interest: " + str(interest))
print("Total account after " + str(months) + " months: " + str(total_account))
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
> Total account after 6 months: 1081
```

## Solution
```Python
deposit_sum =    int(input("deposit sum:"))
interest_rate =  float(input("interest rate in %:"))
tax_rate =       float(input("tax in %:"))
months =         int(input("nuber of months:"))

interest = deposit_sum * (interest_rate/100) * (months/12)
taxes = interest * (tax_rate/100)
interest_after_tax = interest - taxes
total_account = deposit_sum + interest_after_tax

print("Deposit: " + str(deposit_sum))
print("Interest rate: " + str(interest_rate) + "%")
print("Period of deposit: " + str(interest_rate) + " months")
print("Interest: " + str(interest_after_tax))
print("Total account after " + str(months) + " months: " + str(total_account))
```
