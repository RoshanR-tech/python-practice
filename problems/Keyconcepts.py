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




# Even or Odd Checker
# Concept: modulus operator, conditionals

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")




# Factorial Program
# Concept: for loop, functions

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))



# Multiplication Table
# Concept: for loop

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)



# Palindrome Checker
# Concept: string slicing

text = input("Enter a word: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


#Range function 
for i in range(1,5):
    for j in range(1,i+1):
        print("*" , end=" ")
    print()



