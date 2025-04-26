# Changing List Elements

list1 = [3, 5, 7, 9, 11, 13, 15]

list2 = list1.copy()
list3 = list1.copy()
list4 = list1.copy()

#####[,) for indexing in every case

list2[1:3] = [88, 99]
print("Changing 2nd and 3rd list elements", list2)

list3[1:3] = [88]
print("Removing two  list elements and adding one", list3)

list4[1:2] = [33, 333]
print("replce 2nd and add teo new values", list4)
