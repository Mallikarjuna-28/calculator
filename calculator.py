a = float(input("Enter first number: "))
op = input("Enter operator (+ - * /): ")
b = float(input("Enter second number: "))

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        print("Cannot divide by zero")
        exit()
    result = a / b
else:
    print("Invalid operator")
    exit()

print("Result:", result)
