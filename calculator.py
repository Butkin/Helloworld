class Calculator:
    print("The calculator has been started!")

    def __init__(self):
        self.subtraction()
        self.addition()
        self.multiplication()
        self.division()
        self.integer()
        self.modulus()
        self.power()


    def addition():
        print(first + second)

    def subtraction():
        print(first - second)

    def multiplication():
        print(first * second)

    def division():
        print(first / second)

    def integer():
        print(first // second)

    def modulus():
        print(first % second)

    def power():
        print(first ** second)

first = float(input("Set first value: "))
second = float(input("Set second value: "))
calculations = str(input("What are going to calculate? (+) (-) (*) (/) (//) (%) (**)?:  "))

print( "Twoje wartości to:")
print( "                    - pierwsza wartość =  ", str(first))
print( "                    - druga wartość    =  ", str(second))
print( "Wybrałeś działanie: "+str(calculations))

if calculations == "+":
    print(Calculator.addition())
    print("To działa!")
    print(first + second)
elif calculations == "-":
    print(Calculator.subtraction())
elif calculations == "*":
    print(Calculator.multiplication())
elif calculations == "/":
    print(Calculator.division())
elif calculations == "//":
    print(Calculator.integer())
elif calculations == "%":
    print(Calculator.modulus())
elif calculations == "**":
    print(Calculator.power())



