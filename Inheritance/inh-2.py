# 2 - Multiple Inheritance
# multiple parents and 1 child class.

# Using 3 parent classes


class Calc1:
    def sum(self, a, b):
        return a + b


class Calc2:
    def sub(self, a, b):
        return a - b


class Calc3:
    def mul(self, a, b):
        return a * b


class Derived(Calc1, Calc2, Calc3):  # Multiple Inheritance
    def div(self, a, b):
        return a / b


# Derived class object can aceess functions from all three parent classes
ob = Derived()
print(ob.sum(10, 20))
print(ob.sub(25, 5))
print(ob.mul(5, 10))
print(ob.div(10, 2))
