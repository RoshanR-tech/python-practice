# ==========================================
# Day 9 - Functions Practice Problems
# Author: Roshan R
# Topic: Python Functions (Basics)
# ==========================================


# ------------------------------------------
# Problem 1: Simple function to print a greeting
# Concept: Basic function definition and call
# ------------------------------------------

def greet():
    print("Hello, welcome to Python functions!")

greet()



# ------------------------------------------
# Problem 2: Function with parameter
# Concept: Passing values into functions
# ------------------------------------------

def greet_user(name):
    print("Hello", name)

greet_user("Roshan")



# ------------------------------------------
# Problem 3: Function to add two numbers
# Concept: Parameters and calculation
# ------------------------------------------

def add_numbers(a, b):
    result = a + b
    print("Sum:", result)

add_numbers(5, 7)



# ------------------------------------------
# Problem 4: Function with return value
# Concept: return vs print
# ------------------------------------------

def multiply(a, b):
    return a * b

answer = multiply(4, 6)
print("Multiplication:", answer)



# ------------------------------------------
# Problem 5: Understanding None output
# Concept: Function without return gives None
# ------------------------------------------

def show_number(num):
    print("Number is:", num) 

result = show_number(10)
print(result)   # This prints None



# ------------------------------------------
# Problem 6: Function to check even or odd
# Concept: Conditional logic inside function
# ------------------------------------------

def check_even_odd(num):
    if num % 2 == 0:      #To check if it is even 
        return "Even"  
    else:
        return "Odd"

print(check_even_odd(8))



# ------------------------------------------
# Problem 7: Function to find square of a number
# Concept: Return values
# ------------------------------------------

def square(num):
    return num * num

print("Square:", square(9))
