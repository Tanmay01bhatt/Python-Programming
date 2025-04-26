# copy dictionaries
# dict1 = dict2 is wrong
# since dict2 is only a ref to dict1
# therefore changes made in dict1 are also reflected in dict2

# copy()

dict1 = {"name": "Tanmay", "age": 24, "loc": "India"}
dict2 = dict1.copy()
print("Dictionary copied", dict2)

# Using the dict constructor

dict3 = dict(dict1)
print("Dictionary copied using constructor", dict3)
