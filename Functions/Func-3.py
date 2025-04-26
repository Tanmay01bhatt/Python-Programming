# Keyword Argument
# sent key = word pair as the arg


def func(name1, name2):
    print("Second", name2)


func(name2="Tanmay", name1="Bhatt")  # Order Doesn't Matter


# Arbitrary Keyword Argument(**kwargs)

# we don't know the no. of keyword arguments to be passed
# the function recieves a dictionary


def func2(**name):
    print("Last name is ", name["last"])


func2(first="Tanmay", last="Bhatt")
