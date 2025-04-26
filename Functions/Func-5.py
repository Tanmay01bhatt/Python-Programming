# Position only Arguments
# Use  ' ,/ ' AFTER THE ARG
# Do not accept Keyword arg


def func(arg, /):
    print(arg)


func(4)

# func(arg=3)  Error

# Keyword Only Arguments
# Use ' *, ' BEFORE THE ARG
# Do not accept positional arg


def func2(*, kwargs):
    print(kwargs)


func2(kwargs=99)
# func2(99)   ERROR

# Position only + Keyword only


def func3(a, b, /, *, c, d):
    print(a + b + c + d)


func3(10, 20, c=30, d=40)
