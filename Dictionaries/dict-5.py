# Loops = only for is used

dict1 = {"name": "Tanmay", "age": 24, "loc": "India"}

# print all keys

for x in dict1:
    print("Key:", x)

# print all values

for x in dict1:
    print("Value:", dict1[x])

# print all keys using keys() method

for x in dict1.keys():
    print("Key", x)

# print all values using the values() method

for x in dict1.values():
    print("Value", x)

# print both keys and values using items() method

for x, y in dict1.items():
    print("Key:", x, "Value:", y)

# Store all keys in a list

list1 = []
for x in dict1:
    list1.append(x)

print("List of keys", list1)
