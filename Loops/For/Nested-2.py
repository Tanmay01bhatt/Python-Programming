# Reverse

rows = 5

for i in range(rows, 0, -1):  # Rows
    for j in range(1, i + 1):  # Pattern
        print(j, end=" ")
    print()
