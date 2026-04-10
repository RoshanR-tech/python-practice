# Number Guessing Game
# Concept: while loop, if-else, user input

secret_number = 7
guess = -1

while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Correct! You guessed it.")
    else:
        print("Wrong guess, try again.")




# Simple Calculator
# Concept: functions, return statement

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"

print(add(5, 3))
print(subtract(10, 4))
print(multiply(2, 6))
print(divide(8, 2))
