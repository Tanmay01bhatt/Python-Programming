# dictionaries = 'key-value'pairs

dict1 = {"name": "Ford", "year": 1964}
print(dict1["name"])

# Duplicates are not allowed
# No two items can have the same key
# the prev vakue will be overwritten
dict2 = {"name": "Ford", "year": 1964, "year": 2024}

print("Dict2", dict2)

# Length
print("Length of dict2", len(dict2))

# Supports all datatypes

# dict3 = {1: "Ford", 2: "BMW", 3: "Volvo"}
dict3 = {
    "name": "Ford",
    "year": 1964,
    "electric": False,
    "colors": ["red", "black", "white"],
}
print("Dict3", dict3)

# Creation
# Normal

dict5 = {"name": "Tanmay", "age": 20}
print("Dict5", dict5)

# Using dict() constructor no (())this time

dict6 = dict(name="Tanmay", age=20)
print(dict6)
