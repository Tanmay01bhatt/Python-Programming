# Sorting == sort()

list1 = ["apple", "zebra", "dog", "cat"]
list2 = [99, 4, 22, 2, 21, 3, 44, 0]

list1.sort()
print("Sorting a list of strings", list1)
list2.sort()
print("Sorting a list of numbers", list2)

# Descending
list2.sort(reverse=True)
print("Sorting a list of numbers in descending order", list2)

list1.sort(reverse=True)
print("Sorting a list of strings in descending order", list1)
