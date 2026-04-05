# Calculator

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = int(input("Choose your arithmatic operation: "))

if operation == 1:
    print(first_number + second_number)
elif operation == 2:
    print(first_number - second_number)
elif operation == 3:
    print(first_number * second_number)
elif operation == 4:
    print(first_number / second_number)
