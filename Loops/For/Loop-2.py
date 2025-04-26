# using range() = 0 to n-1

for x in range(6):
    print(x, end=" ")

print()  # change line

# Changing the default values

for x in range(2, 30, 3):
    print(x, end=" ")

print()

# Use else with for loop

for x in range(6):
    print(x, end=" ")
else:
    print("\nout of range")
