# Accesing items

# []
dict1 = {"name": "Tanmay", "age": 24, "Loc": "India"}

a = dict1["name"]

# or use get()

a = dict1.get("name")
print("Get name", a)


# keys()= get the list of all the keys present in the dictionary

keys = dict1.keys()
print("Keys", keys)

# values()= get the list of all the values present in the dictionary
values = dict1.values()
print("Values", values)

# check if key exists int the dictionary

if "Loc" in dict1:
    print("Key  exists")

# items(): get a list of key : value pairs

x = dict1.items()
print("Items", x)
