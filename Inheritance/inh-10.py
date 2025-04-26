# (D) - passing arguments using super


class Parent:
    def __init__(self, name):
        print("NAME :", name)


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # passing the argument
        print("AGE:", age)


ob = Child("Tanmay", 24)
