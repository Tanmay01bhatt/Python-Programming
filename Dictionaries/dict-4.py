# Remove Items

dict1 = {"name": "Tanmay", "age": 24, "loc": "India"}

# By Index

# pop()

dict1.pop("age")
print("Item reomved", dict1)

# Only remove the last Item
# popitem()

dict1.popitem()
print("Last Item reomved", dict1)

# using del keyword

# del dict1["loc"]

# clear the dictionary = clear()

dict1.clear()
print("Cleared Dictionary", dict1)
