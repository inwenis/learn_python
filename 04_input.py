# input() will make the program stop and wait for the user to input
# some text and press [enter]

# input() will return text inputted by the user, we can store it in a
# variable (see below)

# usually before a input() we use a print() to let the user know
# that we expect him to type something
print("Please describe today's weather and press [enter]")
weather_desc = input()
weather_desc_with_wow = "WOW! Is is really " + weather_desc +\
                        "? I love this kind of weather!"
print(weather_desc_with_wow)

print("What country are you from?")
ctry = input()
print("What city are you from?")
city = input()
msg = ctry + city
print("so you're from " + msg)

# Since the user can type anything in the console, we never know if
# the user actually typed a number or some text. This is why input()
# always returns a str and we have to convert it to a int.
print("What year were you born in?")
y_as_text = input()
y = int(y_as_text)
age = 2019 - y
print("You are: " + str(age))

# exercise 1: write a program which will ask the user for his/hers
# name and reply with a:
# "Hello [name here]! I'm flattered to meet you."


# tip: you can "comment out" the code above so you're not asked for
# the weather every time. To "comment out" means to precede a line of
# code with a # sign so that python will treat it as a comment and
# ignore it.


# exercise 2: write a program which will ask the user for two
# numbers, add them and display the sum.
# Important: Make sure you're actually adding the numbers, not
# concatenating text.


# exercise 3: write a program which will ask the user for his/hers
# weight (in kilograms) and height (in meters) and compute BMI*.
# *BMI - Body Mass Index, a convenient rule of thumb allowing to
# categorize a persons weight. BMI = weight / (height * height)
