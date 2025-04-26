# Remove list Items
# 1)List item= remove() method removes the first occurrence of the specified value

list1 = [3, 5, 7, 7, 9, 11, 13, 15]
list1.remove(7)
print("Removing an item from the list", list1)

# 2)Index = pop() method removes the item at the specified index (pos) and returns it
list2 = [3, 5, 7, 9, 11, 13, 15]
list2.pop(2)
print("Removing an item at the specified index", list2)
# if no index is soecified, the pop() method removes the last item in the list
list2.pop()
print("Removing the last item in the list", list2)

# 3) clear() method removes all the items in the list
list3 = [3, 5, 7, 9, 11, 13, 15]
list3.clear()
print("Removing all items in the list", list3)

# 4) del keyword removes the item at the specified index (pos)
list4 = [3, 5, 7, 9, 11, 13, 15]
del list4[2]
print("Removing an item at the specified index", list4)
