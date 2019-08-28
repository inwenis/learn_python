import numpy

for h in numpy.arange(1.5, 2, 0.020)[::-1]:
    print("%.2fm " % h, end="")
    for w in range(40, 150):
        # ------- you should not modify doce above this line --------

        # exercise: Your task is to compute BMI, and based on the BMI
        # assign a text character to the variable bmi_symbol.
        # The code will draw a BMI chart once you have completed the
        # exercise.
        # The variables w and h are already defined and contain:
        # variable w - contains the weigth in kilograms
        # variable h - contains the height in meters
        # bmi_symbol should be assigned a character following rules:
        # for BMI less than 18 assign "<" (less than)
        # for BMI from 18 to 25 assign " " (space)
        # for BMI from 25 to 29 assign "`" (back tick)
        # for BMI above 29 assign "^" (carat)
        # Your code must use the same indentation as the comments you
        # are reading.
        bmi_symbol = " "

        # modify the below if/else so correct characters are assigned
        # to bmi_symbol depending on value of BMI
        if w < 100:
            bmi_symbol = "<"
        elif h > 1.8:
            bmi_symbol = "t"



        # ------- you should not modify below below this line -------
        print(bmi_symbol, end = "")
    print()

print("      ", end="")
for w in range(40, 150, 10):
    print(str(w) + "kg      ", end="")
print()