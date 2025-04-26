# Join Sets Operations

# Union combines two sets and returns a new set with all items from both sets

set1 = {1, 2, 3}
set2 = {"a", "b", "c"}

set3 = set1.union(set2)
print("Union of two sets", set3)

set5 = set1 | set2  # another way to do union
set6 = {5, 6, 7}
set7 = set1.union(set2, set6)
print("UNION of multiple sets", set7)

# union returns a new set whereas update does not.

# Intersection returns a new set with only the items that are present in both sets(duplicates/common element)

sett1 = {1, 2, 3}
sett2 = {3, True, 5}

set4 = sett1.intersection(sett2)
sett4 = sett1 & sett2  # another way to do intersection
print("Intersection", set4)


# Diffference =  returns items present int the first set but not in the second
settt1 = {1, 2, 3}
settt2 = {3, 4, 5}
sett5 = settt1.difference(settt2)
sett5 = settt1 - settt2  # another way to do difference
print("Difference", sett5)


# Symmetric Difference = returns items that are in either set but not in both sets(no duplicates)

sett6 = settt1.symmetric_difference(settt2)
sett6 = settt1 ^ settt2  # another way to do symmetric difference
print("Symmetric Difference", sett6)
