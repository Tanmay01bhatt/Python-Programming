# Remove Set Items

set1 = {44, 77, 88, 99, 33}

# remove = gives an error if values doesn't exist
# discard = doesn't give an error

set1.remove(44)
print(set1)

# set1.remove(123)  gives an error

set1.discard(99)
print(set1)

set1.discard(123)  # no error

# pop() = randomly removes an item

set2 = {23, 34, 45, 67}
set2.pop()
print(set2)


# clear() = empties the set

set2.clear()
print(set2)
