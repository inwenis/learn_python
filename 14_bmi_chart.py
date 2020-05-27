# ------- you should not modify code above this line --------

# exercise: Your task is to compute BMI, and based on the BMI
# assign a text character to the variable bmi_symbol.
# The code will draw a BMI chart once you have completed the
# exercise.
# The variables w and h are already defined and contain:
# variable w - contains the weight in kilograms
# variable h - contains the height in meters
# bmi_symbol should be assigned a character following rules:
# for BMI less than 18 assign "<" (less than)
# for BMI from 18 to 25 assign " " (space)
# for BMI from 25 to 29 assign "`" (back tick)
# for BMI above 29 assign "^" (carat)
# Your code must use the same indentation as the comments you
# are reading.

# modify the below if/else so correct characters are assigned
# to bmi_symbol depending on value of BMI

# Solution

def bmi_to_symbol(w, h):
    bmi = w / (h*h)
    if bmi < 18:
        bmi_symbol = "<"
    elif bmi < 25:
        bmi_symbol = "."
    elif bmi < 29:
        bmi_symbol = "^"
    else:
        bmi_symbol = ">"
    return bmi_symbol

for h in [x * 0.02 + 1.5 for x in range(0,26)][::-1]:
    print("%.2fm " % h, end="")
    for w in range(40, 150):
        symbol = bmi_to_symbol(w, h)
        print(symbol, end = "")
    print()

print("      ", end="")
for w in range(40, 150, 10):
    print(str(w) + "kg      ", end="")
print()

# TODO add legend
