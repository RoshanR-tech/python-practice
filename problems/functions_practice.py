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





#mini problem code  
def square(n):
    return n*n
    
def cube(n):
    return n*square(n)
    
def power_sum(n):
    return cube(n)+square(n)

n = int(input("Enter your number: "))
   
result1 = square(n)
result2 = cube(n)
result3 = power_sum(n)

print("square",result1)
print("cube",result2)
print("power sum",result3)





#General calculator 
def calc(a, b, operation="add"):

    if operation == "add":
        return a + b

    elif operation == "sub":
        return a - b

    elif operation == "mul":
        return a * b

    elif operation == "div":
        if b == 0:
            return "Invalid"
        else :
            return a/b
    else:
        return "Invalid operation"


print(calc(5,3))
print(calc(5,3,"sub"))
print(calc(5,3,"mul"))
print(calc(5,0,"div"))




#even and odd checker 
def check_even_odd(n):
    
    if n%2==0:
        return "Even"
    else :
        return "Odd"
        
n=int(input("Enter a number: "))
result = check_even_odd(n)
print(result)



#Maximum number finder
def max_of_three(a,b,c):
    
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    elif c>=a and c>=b :
        return c
        
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))

result = max_of_three(a,b,c)
print(f"The largest among {a} , {b} and {c} is :",result)



#normal function 
def add_ten(x):
    return x + 10
print(add_ten(5)) # Output: 15
#lambda function 
add_ten = lambda x: x + 10
print(add_ten(5)) # Output: 15
