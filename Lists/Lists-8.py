# Customize Sort
## key = function
###sort the numbers on the basis of which is closer to 50.

list1 = [99, 4, 22, 2, 21, 3, 44, 0]


def func(x):
    res = abs(x - 50)
    return res


list1.sort(key=func)
print("Sorting a list of numbers using custom function", list1)


## sort()  is Case Sensitive
### Uppercase letters are sorted before lowercase letters.
list2 = ["banana", "Apple", "cherry", "Kiwi"]
list2.sort()
print("Sorting is case sensitive ", list2)

list2.sort(key=str.lower)
print("Sorting is case insensitive ", list2)
