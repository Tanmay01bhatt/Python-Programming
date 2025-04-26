# Global variables

str = "great"

""""
def func():
    print("I am", str)

func()
"""


"""
if the local variable has the same name as that of the class , the global variable remains unchanged
def func2():
    str = "bad"
    print("I am", str)


func2()
print("I am", str)
"""


# Creating a global variable inside a function/chaning the value of a global variable inside a function use keyword global
def func3():
    global str
    str = "bad"


func3()
print("I am", str)
