"""A friendly greeting bot that asks for the user's name."""

print("=== Greeting Bot ===")
name = input("What is your name? ").strip()

if name:
    print(f"Hello, {name}! Welcome. Have a great day!")
else:
    print("Hello, friend! Welcome. Have a great day!")
