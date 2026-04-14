#Single defining for multiple functions
def calculate(a,b):
    addition = a+b 
    difference = a-b
    product = a*b
    return addition, difference, product
a = int(input("Enter a number: "))   
b = int(input("Enter a number: "))   
addition, difference, product = calculate(a, b)
print("Sum =", addition)
print("Difference =", difference)
print("Product =", product)
    

#Functions with and without return values
def add_print(a,b):
    print(a+b)
def add_return(a,b):
    return a+b
    
result1 = add_print(2,2)
result2 = add_return(2,2)
print(result1)
print(result2)
