# Hybrid Inheritance
# combines 2 or more types of inheritances

# Eg:single + multiple


class ceo:
    def fun1(self):
        print("I am the CEO")


class manager(ceo):  # Simple
    def fun2(self):
        print("I am the manager")


class emp1(manager, ceo):  # Multiple
    def func3(self):
        print("I am employee 1")


ob = emp1()
ob.func3()
ob.fun2()
ob.fun1()
