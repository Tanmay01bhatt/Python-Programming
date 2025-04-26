#  class var        vs            instance var
#  classname.var                    obj.var/self.var

#  Changes made affects             Changes made Affects
#  the entire class                 only THAT object


class Person:
    name = "Tanmay"  # class var

    def __init__(self, age):
        self.age = age  # instance var

    def out(self):
        print(f"NAME : {Person.name} AGE : {self.age}")


ob1 = Person(18)
ob2 = Person(30)

ob1.out()  # instance var changes are only reflected to that object.
ob2.out()

Person.name = "Emily"

ob1.out()  # class var changes are reflected throughout the class
ob2.out()


# pass Statement
# class defination can't be empty


class Elect:
    pass
