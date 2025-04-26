# Exception Handling = managing runtime errors

try:
    print(x)
except:
    print("Exception is raised")


# Defining an Exception
# While defining = The error name should be correct

try:
    print(x)
except NameError:
    print("Variable x is not defined")
else:
    print("Nothing went wrong")
