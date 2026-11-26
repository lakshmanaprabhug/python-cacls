"""A simple command-line calculator."""

print("=== Simple Calculator ===")

first_number = float(input("Enter the first number: "))
operator = input("Choose an operation (+, -, *, /): ")
second_number = float(input("Enter the second number: "))

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number == 0:
        print("Error: You cannot divide by zero.")
        result = None
    else:
        result = first_number / second_number
else:
    print("Invalid operation. Please choose +, -, * or /.")
    result = None

if result is not None:
    print(f"Result: {first_number} {operator} {second_number} = {result}")
