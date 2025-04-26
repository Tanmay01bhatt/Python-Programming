# Complete Program


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def output(self):
        print("My name is ", self.name)


class student(Person):
    def __init__(self, name, age, loc):
        super().__init__(name, age)  # args passed
        self.loc = loc

    def output(self):
        super().output()  # parent func called (overriding)
        print("My age is ", self.age, " and I live in ", self.loc)


ob = student("Tanmay", 24, "India")
ob.output()
