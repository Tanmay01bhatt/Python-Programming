# Using the Exception Object
# The Exception Object contains info about the error that occured.


try:
    x = 1 / 0
except Exception as e:
    print("Error Name:", e)
