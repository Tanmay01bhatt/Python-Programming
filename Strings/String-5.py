# String Formatting
# f string

age = 23
txt = f"My name is Tanmay and my age is {age}"
print(txt)

# Placeholder and Modifiers(:)
# MATH              FORMATTING

# modifier
price = 59
print(f"Price of onion is {price: .2f}")

# Placeholder
cost = 49

print(f"The cost is {cost * 10}")

print(f"The cost is {cost / 10}")

print(f"The cost is {cost % 10}")


# Escape Characters

print("Hello\nWorld")  # New line
print("Hello \t World")  # Tab space
print("Hello \\ World")  # Backslash
print('Hello "Hi" World')  # Double Quote
print("Hello\b")  # backspace
