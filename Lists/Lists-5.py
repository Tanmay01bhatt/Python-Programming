# List Loops

# # Looping through a list items

list1 = [3, 5, 7, 9, 11, 13, 15]
print("Looping through a list items")
for item in list1:
    print(item)


# # Looping through a list using index


# for loop
print("Looping through a list using index")
print("for loop")
len1 = len(list1)
for i in range(len1):
    print(list1[i])


# while loop
print("while loop")
i = 0
while i < len1:
    print(list1[i])
    i = i + 1
