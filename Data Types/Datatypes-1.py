a = 20.5
b = 1j
c = ["apple", "banana", "cherry"]
d = range(5)
e = (1, 2, 3)
f = {"name": "John", "age": 30, "city": "New York"}
g = {1, 2, 3, 4, 5}
h = True
i = None


def gettype(var):
    return type(var)


print(gettype(a))  # <class 'float'>
print(gettype(b))  # <class 'complex'>
print(gettype(c))  # <class 'list'>
print(gettype(d))  # <class 'range'>
print(gettype(e))  # <class 'tuple'>
print(gettype(f))  # <class 'dict'>
print(gettype(g))  # <class 'set'>
print(gettype(h))  # <class 'bool'>
print(gettype(i))  # <class 'NoneType'>
