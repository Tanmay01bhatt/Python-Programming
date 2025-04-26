# List Comprehension
# List comprehension is a concise way to create lists in Python.(Shortest syntax)
# Commonly used for creating new lists using old lists.

# Syntax:
# newlist = [expression for item in iterable if condition == True] ]

list1 = [1, 2, 3, 4, 5]
[print(x) for x in list1]

list2 = [x for x in list1 if x > 2]
print(list2)

list3 = ["apple", "banana", "cherry"]
list4 = [x for x in list3 if "a" in x]
print(list4)
list5 = [x.upper() for x in list3]
print(list5)
list5 = ["hello" for x in list3]
print(list5)

list6 = [x if x != "banana" else "orange" for x in list3]
print(list6)

list7 = [x for x in range(10) if x % 2 == 0]
print(list7)
