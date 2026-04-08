# Python calculator

# Creating variables for the user's input
operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Creating an if statement for each operator chosen
if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    if num2 == 0:
        print("You can't divide by zero!")
    else:
        result = num1 / num2
        print(round(result, 3))
else:
    print(f"'{operator}' is not a valid operator")
