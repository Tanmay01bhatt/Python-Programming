# Adding List Items

# append() method adds an item to the end of the list

list1 = [3, 5, 7, 9, 11, 13, 15]
list1.append(17)
print("Adding an item to the end of the list", list1)

# insert() method adds an item at the specified index  (pos,item)
list2 = [3, 5, 7, 9, 11, 13, 15]
list2.insert(2, 88)
print("Adding an item at the specified index", list2)

# Combine two lists using extend() method  #no new list is created
list3 = [3, 5, 7, 9, 11, 13, 15]
list4 = [17, 19, 21]
list3.extend(list4)
print("Combining two lists using extend()", list3)

# combining any two iterables
list5 = [3, 5, 7, 9, 11, 13, 15]
tup = (17, 19, 21)
list5.extend(tup)
print("Combining any two iterables", list5)

# Using + operator to combine two lists == can't cambine two diff iterables
list6 = [3, 5, 7, 9, 11, 13, 15]
list7 = [17, 19, 21]
list8 = list6 + list7
print("Using + operator to combine two lists", list8)
