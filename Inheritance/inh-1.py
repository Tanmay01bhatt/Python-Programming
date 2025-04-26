# Inheritance
# allows a child class to inherit attributes(variables) and methods from the parent class

# 1- Single Inheritance


class Parent:
    def par(self):
        print("Parent class method call")


class Child(Parent):  # Inheritance
    def chil(self):
        print("Child class method call")


ob = Child()  ## Always create the instance of the derived class
ob.par()  # derived class object can aceess the methods from parent class
ob.chil()
