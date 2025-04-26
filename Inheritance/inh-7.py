# super() keyword
# allows us to access the parent class variables and functions from within the child class

# 1 - Simple


class parent:
    def show(self):
        print("Parent Method")


class child(parent):
    def fun(self):
        super().show()  # parent function is called


ob = child()
ob.fun()


# 2-In Method Overfitting


class animal:
    def sound(self):
        print("\nThe animal makes a sound")


class dog(animal):
    def sound(self):
        super().sound()  # parent func call
        print("woof wooof")


ob2 = dog()
ob2.sound()

# TBC...
