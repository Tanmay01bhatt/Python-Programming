# 3- Multi Level Inheritance
# Eg =  Grandparent - Parent - Child


class universe:
    def uni(self):
        print("This is the universe")


class earth(universe):
    def ear(self):
        print("This is earth")


class india(earth):
    def ind(self):
        print("This is India")


# This child object can access all three classes
ob = india()
ob.ind()
ob.ear()
ob.uni()
