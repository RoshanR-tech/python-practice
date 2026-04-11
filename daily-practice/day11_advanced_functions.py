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
    
    
