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
