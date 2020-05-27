# exercise: I started coding a program to print a BMI chart. I didn't
# finish it. There are 2 functions to be finished so the program can
# work.
# Your task is to complete these functions and run the program.

# w - contains the weight in kilograms
# h - contains the height in meters
# bmi_to_symbol() should return a character based on the bmi:
# - BMI less than 18 return "<" (less than)
# - BMI from 18 to 25 return "." (dot)
# - BMI from 25 to 29 return "x"
# - BMI above 29 return ">" (greater than)
def bmi_to_symbol(w, h):
    # TODO: complete the bmi_to_symbol function.
    bmi = w / (h*h)
    if bmi < 18:
        bmi_symbol = "<"
    elif bmi < 25:
        bmi_symbol = "."
    elif bmi < 29:
        bmi_symbol = "x"
    else:
        bmi_symbol = ">"
    return bmi_symbol

# The range() funciton returns a range of integers. For the chart to
# be printed we need a simillar function returning a range of floats.
# Finish float_range(beg, end, step) function.
# The function should return a list of float values starting from
# `beg` and up till `end` with step equal to `step`.
# Example: float_range(1.0, 1.5, 0.1) should return
# [1.0, 1.1, 1.2, 1.3, 1.4]
# Example: float_range(0, 10, 1.5) should return
# [0, 1.5, 3.0, 4.5, 6.0, 7.5, 9.0]
# tip: you'll need to create a list and append values to it in a loop
def float_range(beg, end, step):
    # TODO: complete the float_range function.
    iter = int((end - beg) / step)
    return [beg + x * step for x in range(0, iter)]

# --------------- do not modify code below this line ----------------
print()
print("                                                   BMI Chart")
print()

for h in float_range(1.5, 2.02, 0.02)[::-1]:
    print("%.2fm " % h, end="")
    for w in range(40, 150):
        symbol = bmi_to_symbol(w, h)
        print(symbol, end = "")
    print()

print("      ", end="")
for w in range(40, 150, 10):
    print(str(w) + "kg      ", end="")
print()

print()
print("x-axis - weight in kilograms")
print("y-axis - height in meters")
print()
print("LEGEND")
print("< - Underweight")
print(". - Normal")
print("x - Overweight")
print("> - Obese")
