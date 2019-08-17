# to execute some code only if a condition is meet use an "if"
cur_year = 2019
print("what year were you born? (type it and press [enter])")
bth_year_as_text = input()
bth_year = int(bth_year_as_text)
if cur_year - bth_year_as_text > 18:
    print("let's get a beer!")
    # like with a while loop code must be indended
    # there can be many lines of code here
    print("since you're 18")

# to execute some code when our condition is not meet use an "else":
# to check if two values are equal we use "=="
print("do you like pyton? (type yes/no and press [enter])")
answer = input()
if answer == "yes":
    print("no wonder!")
else:
    print("I'll give you one more try")

# we can check for multiple conditions with elif:
print("do you like pyton? (type yes/maybe/no and press [enter])")
answer = input()
if answer == "yes":
    print("no wonder!")
elif answer == "maybe":
    print("love needs its time")
elif answer == "no":
    print("I don't belive you")
else:
    print("what do you mean by: '" + answer + "' ?")

# a "while" loop can be nested under an "if"
# a "if/elif/else" can also be nested under a "while" loop
print("on a 1-10 scale, how well are you today? (type and press [enter])")
happiness = int(input())
if happiness > 5:
    i = 0
    while i < happiness:
        print("happy!")
        i = i + 1

# exercie 1: modify the asterisks-triangle program so that it will not
# print triangles higher than 20. When the user input a number greater
# than 20 we should inform him that the number is too large

# exercise 2: modify the asterisks-triangle program so that it will
# also print triangles of height 20-30 but preceed them with a message:
# "you're quite demanding, but I'll manage!"

# exercise 3: extend the asterisks-triangle program so that it will
# also print triangles of height 30-40 but preceed them with a message:
# "watch out! you're near the limit!"
