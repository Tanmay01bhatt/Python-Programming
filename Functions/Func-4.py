# Default Parameter Value
# Executed when no arg is passed


def func(age=18):
    print("Age is:", age)


func(24)
func(99)
func()
func(2)


# Passing A List As An Argument


def func2(food):
    for x in food:
        print(x, end=" ")


fruits = ["apple", "cheery", "grape", "mango"]
func2(fruits)


# return values
# Lets a Function retrun a value


def func3(x):
    return 5 * x


print()
print(func3(3))
print(func3(5))
print(func3(9))


# pass statement


def my_func(x):
    pass
