# Creation

# Normal

set1 = {"a", "b", "c"}

# Using  a constructor (())

set2 = set((44, 66, 78, 98))

print("sets", set1, set2)

# Accessing set items
# Can't access through Index since there is none
print("Looping through a set")
for item in set2:
    print(item, end=" ")
