# Assigning values from a tuple/unpacking a tuple
tup1 = (22, 55, 66)
a, b, c = tup1
print(a, b, c)


# use * if var are less than values to assign the remaining values to a list
tup2 = (22, 32, 4, 5, 55, 6, 7, 77)

x, *y, z = tup2
print(x, y, z)
