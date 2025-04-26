# Nested Dictionaries

# First method

dictionary1 = {
    "dict1": {"name": "Tanmay", "age": 24},
    "dict2": {"name": "Rohan", "age": 25},
    "dict3": {"name": "Mohan", "age": 27},
}


# Second Method =create seprate and combine later

dic1 = {"car": "BMW", "model": "X5"}
dic2 = {"car": "Ford", "model": "Mustang"}
dic3 = {"car": "Audi", "model": "A8"}

dictionary2 = {"dic1": dic1, "dic2": dic2, "dic3": dic3}

# Access Items

print(dictionary1["dict1"]["name"])
print(dictionary2["dic3"]["car"])


# Loop through the nested dictionaries

for x, y in dictionary1.items():
    print(x)  # x=dict name y = dictionary itself

    for z in y:
        print("Key:", z, "Value:", y[z])
