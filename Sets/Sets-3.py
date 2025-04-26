# add() =Adds Set Items

set1 = {33, 55, 45, 67, 52}
set1.add(1034)
print("New Set", set1)

# update() =  adds another any iterable
# no new set is created
set2 = {"apple", "banana", "grape"}
set3 = {6, 7, 8}
set2.update(set3)
print("secind new set", set2)

tup = (True, False)
set3.update(tup)
print("Newest set", set3)
