# Copy Lists

# list1 = list2 is wrong since list2 will only be a reference to list1 and any changes made to list1 will also affect list2.

# copy()
list1 = [3, 5, 7, 9, 11, 13, 15]
list2 = list1.copy()
print("Copying a list using copy()", list2)

# Use the list constructor
list3 = [99, 88, 77]
list4 = list(list3)
print("Copying a list using list constructor", list4)

# Use slicing
list5 = list3[:]
print("Copying a list using slicing", list5)
