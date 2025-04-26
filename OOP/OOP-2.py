# Parameterized constructor


class Person:
    def __init__(self, name, age):  # Parameterized Constructor
        self.name = name
        self.age = age

    def fuc(self):
        print("Name id:", self.name, "Age id:", self.age)


age = int(input("Enter your age "))
name = input("Enter your name ")

obj = Person(name, age)
obj.fuc()
