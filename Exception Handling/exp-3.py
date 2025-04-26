# Multiple Except Blocks

try:
    num = int(input("Enter a number :"))
    result = 100 / num
    print("Result = ", result)
except ZeroDivisionError:
    print("Can't divide by zero")
except ValueError:
    print("Not a valid number")
