# Method Overriding
# When a child class defines a functions with the name name as the function that already exists in the parent class
# Then the parent class function gets overridden.


class animal:
    def speak(self):
        print("The animal makes a sound")


class dog(animal):
    def speak(self):  # Overriden
        print("The dog barks")


ob = dog()
ob.speak()
