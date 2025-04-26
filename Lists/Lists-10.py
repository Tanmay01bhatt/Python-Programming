# Join Lists
# concatenate two lists using the + operator

list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
list3 = list1 + list2
print("Join Lists", list3)

# Join Lists using the extend() method == no new list is created
list4 = [1, 2, 3]
list5 = ["a", "b", "c"]
list4.extend(list5)
print("Join Lists using the extend() method", list4)

# Join Lists using the append() method == no new list is created
list6 = [1, 2, 3]
list7 = ["a", "b", "c"]
for item in list7:
    list6.append(item)
print("Join Lists using the append() method", list6)
