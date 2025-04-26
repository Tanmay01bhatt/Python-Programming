# lambda is best used inside another function

# Double/Triple/Quad the given number


def func(n):
    return lambda a: a * n


dob = func(2)

quad = func(4)

print(dob(11))
print(quad(11))
