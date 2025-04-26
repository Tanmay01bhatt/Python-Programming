# Loops Through:

# Items

tup1 = (55, 66, 87, 5)
for x in tup1:
    print(x, end=" ")
print()


# Index
# for
tup2 = (5, 66, 432, 445, 86, 78, 99)
len1 = len(tup2)

for i in range(len1):
    print(tup2[i], end=" ")
print()


# while

tup3 = (22, 44, 55, 77, 99, 77, 88)
len2 = len(tup3)
i = 0
while i < len2:
    print(tup3[i], end=" ")
    i = i + 1
print()

# multiplying a tuple

tup5 = (2, 5)
tup5 = tup5 * 2
print(tup5)
