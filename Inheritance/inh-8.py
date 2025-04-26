# super()
# 3- In Multiple Inheritance

# To follow MRO = Method Resolution Order
# sequence in which python searches for a method or attribute when called by an object
# OR
# seq in which a method is searched  by python in a class hierarchy.


class A:
    def out(self):
        print("A")


class B(A):
    def out(self):
        print("B")
        super().out()  # parent method call


class C(A):
    def out(self):
        print("C")
        super().out()


class D(B, C):
    def out(self):
        print("D")
        super().out()


ob = D()
ob.out()

# checking MRO using an attribute
print(D.__mro__)


# if super() was not used  o/p :- DBACA
# 'A' would be called twice
