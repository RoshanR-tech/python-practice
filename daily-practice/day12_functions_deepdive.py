#Task 1
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b == 0 :
        return "cannot be divided by 0"
    else :
        return a/b 


#Print vs Return functions 
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b == 0 :
        return "cannot be divided by 0"
    else :
        return a/b 


#multiple functions with nested functions
def square(n):
    return n*n
def double(n):
    return n*2
    
result = square(double(5))
print(result)
