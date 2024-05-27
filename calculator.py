import os
from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}

def calculator():

  print(logo)

  n1 = float(input("What's the first number? "))
  print()

  for key in operations:
      print(key)
  print()

  direction = "y"
  while direction == "y":
    operation = input("Pick an operation: ")
    while operation != "+" and operation != "-" and operation != "*" and operation != "/":
        operation = input("Pick an operation: ")
    print()

    n2 = float(input("What's the next number? "))
    print()

    answer = operations[operation](n1=n1, n2=n2)

    print(f"{n1} {operation} {n2} = {answer}")
    print()

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
        n1 = answer
    else:
        os.system('cls')
        calculator()
    print()

calculator()