# to execute some code only if a condition is meet use an "if"
cur_year = 2019
print("what year were you born? (type it and press [enter])")
bth_year_as_text = input()
bth_year = int(bth_year_as_text)
if cur_year - bth_year > 18:
    print("let's get a beer!")
    print("since you're at least 18")
    # there can be many lines of code here under an if
    # as long as the code is indented it will be only executed if the
    # condition from "if" is meet
    print("you are " + str(cur_year - bth_year) + " years above 18.")


# to execute some code when our condition is not meet use an "else":
print("----- same code now with an 'else' ------")
cur_year = 2019
print("what year were you born? (type it and press [enter])")
bth_year_as_text = input()
bth_year = int(bth_year_as_text)
if cur_year - bth_year > 18:
    print("let's get a beer!")
    print("since you're 18")
    print("you are " + str(cur_year-bth_year) + " years above 18.")
else:
    print("no beers for you my friend!")


# Important!
# The value stored in a variable can be updated/changed. We can
# change it's value as many times as required:
x = 10
print(x) # x is now 10
x = 50
print(x) # x is now 50
# we can even use the current value of x, add something to it and
# store it back to x
x = x + 3
print(x) # x is now 53

# The same applies to str variables of other types
a = "I like"
a = a + " apples"
print(a)


# we can check for multiple conditions with elif:
p = 50
print("p is now " + str(p) + ". Would you like to add/remove 1 from it?")
answer = input()
if answer == "add":
    p = p + 1
elif answer == "remove":
    p = p - 1
else:
    print("sorry, what do you mean by " + answer + " ?")
print("p is now " + str(p))
# notice that to check if two vlaues are equal we use "==" . This is
# beacuse the single equal sign "=" already means "assign value" in
# Python.

# conditions can be nested:
print("did you sleep well today? (type yes/no and press [enter])")
slept_well = input()
if slept_well == "yes":
    print("I'm happy for you")
else:
    print("did you remember to not watch youtube in bed? (type yes/no and press [enter])")
    watched_youtube = input()
    if watched_youtube == "yes":
        print("That's wise")
    else:
        print("maybe that's the issue?")

# What kind of check can we have in a "if" or "elif"?
# - test if values are equal ==
# - test if greater          >
# - test if less             <
# - test if greate or equal  >=
# - test if less or equal    <=

# To check for multiple condiditons we use a "and" or "or"
print("Let's see if you're in you twenties.")
print("What is your age? (type and press [enter])")
age_as_text = input()
age = int(age_as_text)
if age >= 20 and age <= 29:
    print("so you're in your twenties")

# exercise 1: Modify the BMI program from previous chapter so that it
# will display the users BMI and display which category his/hers BMI 
# falls into.
# BMI less than 25 is category "Normal"
# BMI from 25 to 29 is "Overweight"
# BMI from 30 is "Obese"


# exercise 2: Modify the BMI program to include all WHO categories.
# | Category                                BMI (kg/m2)
# |                                       | from | to   |
# -------------------------------------------------------
# | Very severely underweight             |      | 15   |
# | Severely underweight                  | 15   | 16   |
# | Underweight                           | 16   | 18.5 |
# | Normal (healthy weight)               | 18.5 | 25   |
# | Overweight                            | 25   | 30   |
# | Obese Class I (Moderately obese)      | 30   | 35   |
# | Obese Class II (Severely obese)       | 35   | 40   |
# | Obese Class III (Very severely obese) | 40   | 45   |
# | Obese Class IV (Morbidly Obese)       | 45   | 50   |
# | Obese Class V (Super Obese)           | 50   | 60   |
# | Obese Class VI (Hyper Obese)          | 60   |      |
