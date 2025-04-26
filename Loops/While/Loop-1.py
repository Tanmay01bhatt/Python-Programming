# while loop
# executes as long as the condition is true

i = 1

while i < 10:
    print(i, end=" ")
    i = i + 1
print()


# break statement = loop stops as soon as break is executed

i = 1
while i < 10:
    print(i, end=" ")
    if i == 6:
        break
    i = i + 1
print()


# continue = skips tthe current iteration and continues execution

i = 0
while i < 6:
    i = i + 1
    if i == 3:
        continue
    print(i, end=" ")
