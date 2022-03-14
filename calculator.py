class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.init()
        print("The calculator has been started!")

    def addition(self):
        print(first + second)

    def subtraction(self):
        print(first - second)

    def multiplication(self):
        print(first * second)

    def division(self):
        print(first / second)

    def integer(self):
        print(first // second)

    def modulus(self):
        print(first % second)

    def power(self):
        print(first ** second)


first = float(input("Set first value: "))
second = float(input("Set second value: "))
aritmatic = input("What are going to calculate? (+) (-) (*) (/) (//) (%) (**)?:  ")

if aritmatic == "+":
    print()