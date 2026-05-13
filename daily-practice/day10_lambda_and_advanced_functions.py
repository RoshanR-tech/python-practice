#normal function
def add(a,b):
    return a+b
#lambda function
add = lambda a,b : a+b


#lambda functions
cube = lambda n : n*n*n
subtract = lambda a,b : a-b
is_even = lambda n : n%2==0 
print(cube(3))
print(subtract(2,3))
print(is_even(2))



#multiple functions
def multiplication(a,b):
    return a*b

def greater(a,b):
    if a>b :
        return a
    else :
        return b 
        
def is_positive(n):
    if n > 0 :
        return "True"
    else :
        return "False"
        
print(multiplication(2,3))
print(greater(2,3))
print(is_positive(3))

#basic mathematic function 
a = int(input("enter a number")
b = int(input("enter a number")
add = lambda a,b : a+b
substract = lambda a,b : a-b
multiply = lambda a,b : a*b

# ============================================
# DAY 10 – FUNCTIONS PRACTICE
# Topics covered:
# 1. Global keyword
# 2. Return vs Print
# 3. Lambda functions
# 4. Common mistakes
# 5. Practice tasks
# ============================================


# ============================================
# 1. GLOBAL KEYWORD EXAMPLE
# Used to modify a global variable inside a function
# ============================================

x = 10

def change_value():
    global x
    x = 20

change_value()

print("Global value:", x)



# ============================================
# 2. RETURN VS PRINT DIFFERENCE
# Print only displays value
# Return sends value back to caller
# ============================================

def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

add_print(5,3)

result = add_return(5,3)
print("Returned value:", result)



# ============================================
# 3. FUNCTION RETURNING NONE (COMMON CONFUSION)
# If return is not used, function returns None
# ============================================

def show():
    print("Hello")

value = show()

print(value)



# ============================================
# 4. LAMBDA FUNCTION (ANONYMOUS FUNCTION)
# Used for short operations
# ============================================

square = lambda x : x * x

print("Square:", square(5))


add = lambda a,b : a+b

print("Sum:", add(4,6))



# ============================================
# 5. NORMAL FUNCTION VS LAMBDA
# Normal functions are better for complex logic
# Lambda is good for short expressions
# ============================================

def cube(x):
    return x*x*x

cube_lambda = lambda x : x*x*x

print("Cube normal:", cube(3))
print("Cube lambda:", cube_lambda(3))



# ============================================
# 6. PRACTICE TASKS
# ============================================

# Task 1: Check even or odd

check = lambda x : "Even" if x%2==0 else "Odd"

print(check(7))


# Task 2: Find maximum of two numbers

maximum = lambda a,b : a if a>b else b

print("Maximum:", maximum(10,25))


# Task 3: Multiply three numbers

multiply = lambda a,b,c : a*b*c

print("Product:", multiply(2,3,4))



# ============================================
# 7. COMMON MISTAKES LEARNED
# ============================================

# Mistake 1: Forgetting return

def test():
    5+5

print(test())   # Returns None


# Correct version

def test2():
    return 5+5

print(test2())



# Mistake 2: Expecting print to store value

def number():
    print(100)

x = number()

print(x)   # None because print does not return value


# ============================================
# DAY 10 SUMMARY
# Learned:
# - Global keyword
# - Return vs print
# - Lambda functions
# - Function mistakes
# - Code organization
# ============================================
