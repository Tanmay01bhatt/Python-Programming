# Hierarical Inheritance
# opposite of multiple inheritance
# 1 parent and Multiple child


class manager:
    def man(self):
        print("Manager")


class emp1(manager):
    def out1(self):
        print("employee 1")


class emp2(manager):
    def out2(self):
        print("employee 2")


# Child class objects

ob1 = emp1()
ob2 = emp2()

ob1.man()
ob1.out1()

ob2.man()
ob2.out2()
