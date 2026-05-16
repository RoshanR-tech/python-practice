# Mini Project 2 - Scientific Calculator in Python
# Concepts used: functions, loops, math module, conditionals

import math #for mathematical functions 

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a/b

def power(a,b):
    return a**b

def square_root(a):
    return math.sqrt(a)

def factorial(a):
    return math.factorial(a)

def sine(a):
    return math.sin(a)

def cosine(a):
    return math.cos(a)

while True:

    print("\n--- Scientific Calculator ---")

    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("5 Power")
    print("6 Square Root")
    print("7 Factorial")
    print("8 Sine")
    print("9 Cosine")
    print("10 Exit")

    choice = int(input("Enter choice: "))

    if choice == 10:
        print("Calculator closed")
        break

    if choice in [1,2,3,4,5]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    elif choice in [6,7,8,9]:
        num1 = float(input("Enter number: "))

    if choice == 1:
        print("Result:", add(num1,num2))

    elif choice == 2:
        print("Result:", subtract(num1,num2))

    elif choice == 3:
        print("Result:", multiply(num1,num2))

    elif choice == 4:
        print("Result:", divide(num1,num2))

    elif choice == 5:
        print("Result:", power(num1,num2))

    elif choice == 6:
        print("Result:", square_root(num1))

    elif choice == 7:
        print("Result:", factorial(int(num1)))

    elif choice == 8:
        print("Result:", sine(num1))

    elif choice == 9:
        print("Result:", cosine(num1))

    else:
        print("Invalid choice")
