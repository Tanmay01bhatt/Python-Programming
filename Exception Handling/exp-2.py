# finally - is ALWAYS executed , regardless of an error

try:
    print(x)
except NameError:
    print("Variable x is not defined")
finally:
    print("Try Except block is executed")
