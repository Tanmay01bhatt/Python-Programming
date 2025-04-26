list1 = ["apple", "banana", "cherry"]
len1 = len(list1)
print("Length", list1)

# data types

list2 = ["apple", 22, 3.5, True, None]
print("supports all datatypes", list2)

print("type of a list", type(list2))

# Creation of a list using a constructor

list3 = list(("apple", "banana", "cherry"))
print("list created using constructor", list3)

# Accessing list items

list4 = [3, 5, 7, 9, 11, 13, 15]
print("Accessing first items", list4[0])
print("Accessing last items", list4[-1])
print("Accessing range of items", list4[1:4])
print("Accessing range of items", list4[:3])
print("Accessing range of items", list4[2:])

# Checking if an item exists in a list
list5 = [1, 2, 3, 4, 5]
if 2 in list5:
    print("2 is present in the list")
else:
    print("2 is not present in the list")
