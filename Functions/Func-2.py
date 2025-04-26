# Arbitrary Arguments (*args)

# when we don't know how many arguments will be passed into your function,
# The Function then recieves a 'TUPLE' of arg values which can be accessed acc.


def func(*name):
    print("Name of second string:", name[1])


func("jon", "tom", "ron", "freddie")
