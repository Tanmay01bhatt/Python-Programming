# 4 - In a Constructor

# (A)- if there is no child class constructor then on object creation , the parent class cons is called


class parent:
    def __init__(self):
        print("Parent class")


class child(parent):
    pass


ob = child()


# (B) - The child class constructor will override the parent class constructor if super() is NOT used.


class Base:
    def __init__(self):
        print("Base Class")


class Derived(Base):
    def __init__(self):
        print("\nDerived")


ob2 = Derived()


# (C) - Using super()


class Super:
    def __init__(self):
        print("\nSuper Class")


class Sub(Super):
    def __init__(self):
        super().__init__()  # parent constructor call
        print("Sub - Class")


ob3 = Sub()
