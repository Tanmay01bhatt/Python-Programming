# Change Dictionay Values

dict1 = {"name": "Tanmay", "age": 24, "loc": "India"}

# Using key

dict1["age"] = 18
print("Dict1", dict1)

# using update({key:value})

dict1.update({"age": 30})
print("Updated age", dict1)


# ADD New Items To The Dictionary

# Use a new index and assign a value

dict1["color"] = "White"
print("New item added", dict1)

# Use update

dict1.update({"Weight": 70})
print("New item added using update", dict1)
