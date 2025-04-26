# self parameter
# holdss the reference to the CURRENT instance of a class
# Used to access the instance variables and methods of that class.


# It does not have to be named 'self' BUT It has to be the first parameter of the class/constructor/function.

# eg


class Person:
    def __init__(silly, age):
        silly.age = age

    def func(abc):
        print("Age is:", abc.age)


ob = Person(18)
ob.func()


# BUT ALWAYS USE 'self' == naming convension
