# Raising an exception
# choosing to raise an exception if a condition occurs

x = -1

if x < 0:
    raise Exception("No numbers beloew 0 are ALLOWED!!!")


y = "hello"

if not type(y) is int:
    raise Exception("Only integers are allowed")
