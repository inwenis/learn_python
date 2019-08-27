print("Please type in a number which will be tested for parity")
text_input = input()
x = int(text_input)
if x % 2 == 0:
    print("Number " + str(x) + " is even")
else:
    print("Number " + str(x) + " is odd")
