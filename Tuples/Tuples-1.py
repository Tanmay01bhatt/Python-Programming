# Tuples are unchangable i.e they are immutable

tup = ("apple", "banana", "cheery")
len1 = len(tup)
print(len1)

# Tuple with one item
# tup = (1) is WRONG

tup2 = tuple(
    "apple",
)
print(tup2)

# tuples can store any dataype

tup3 = ("apple", 2, True, 40.0)
print(tup3)

# Creation
# (A)simple
tup4 = (22, 44, 66)
print(tup4)

# (B)Using Constructor
tup5 = tuple(("apple", 44, True))
print(tup5)

# Access tuple elements like accessing list items
tup6 = (55, 77, 99, 888)
print(tup6[2])
print(tup6[-1])
print(tup6[0:2])
print(tup6[1:])
