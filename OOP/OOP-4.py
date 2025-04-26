class Person:
    def __init__(self, name, age):  # Parameterized Constructor
        self.name = name
        self.age = age

    def fuc(self):
        print("Name id:", self.name, "Age id:", self.age)


# Deleting an instance variable

obj = Person("Tanmay", 18)
obj.fuc()

del obj.age
# obj.fuc() NO ATRRIBUTE ERROR

# Deleting an object

del obj  # Object is deleted
obj.fuc()
