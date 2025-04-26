# sample java like program in python


class Addition:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def input(self):
        self.a = int(input("Enter value of a "))
        self.b = int(input("Enter value of b "))

    def processing(self):
        self.c = self.a + self.b

    def output(self):
        print("Output :", self.c)


obj = Addition()
obj.input()
obj.processing()
obj.output()
