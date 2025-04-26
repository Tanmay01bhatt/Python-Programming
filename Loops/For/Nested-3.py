# 3 Nested Loops

rows = 5

for i in range(1, rows + 1):  # rows
    for space in range(rows - i):  # spaces
        print(" ", end=" ")

    for j in range(1, i + 1):  # Ascending order
        print(j, end=" ")

    for k in range(i - 1, 0, -1):  # Descending order = reverse loop
        print(k, end=" ")

    print()
