def calc_add(a, b):
    return a + b


def calc_subtract(a, b):
    return a - b


def calc_multiply(a, b):
    return a * b


def calc_divide(a, b):
    return a / b


def calc_power(a, b):
    return a ** b

calculator = True

while calculator:
    operation = input("What operation would you like to do? ADD/SUBTRACT/MULTIPLY/DIVIDE/POWER: ")

    if operation.lower() == "add":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(calc_add(a, b))

    elif operation.lower() == "subtract":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(calc_subtract(a, b))

    elif operation.lower() == "multiply":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(calc_multiply(a, b))

    elif operation.lower() == "divide":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(calc_divide(a, b))

    elif operation.lower() == "power":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(calc_power(a, b))

    calc_question = input("Do you want to do another operation? (Y/N) ")
    if calc_question.lower() == "y":
        calculator = True
    elif calc_question.lower() == "n":
        calculator = False