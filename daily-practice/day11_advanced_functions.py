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

#nested functions
def square(n):
    return n*n
def double(n):
    return n*2
    
result = double(square(3))    #square operation is done first and later moved to double 
print(result)



#Calculator using functions
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return "Cannot be divided by 0"
    else :
        return a/b

print("\n___Menu___")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = int(input("Select a function: "))

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if choice == 1:
    print("Result = ",add(a,b))
    
elif choice == 2:
    print("Result = ",sub(a,b))
    
elif choice == 3:
    print("Result = ",mul(a,b))
    
elif choice == 4:
    print("Result = ",div(a,b))
    
else :
    print("Invalid , enter a number in btw 1-4")    #Detailing 



#using while loop to create a menu driven calculator using functions
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return "Cannot be divided by 0"
    else :
        return a/b

while True:
    print("\n___Menu___")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

    choice = int(input("Select a function: "))


    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
        
    if choice == 1:
        print("Result =", add(a,b))
    elif choice == 2:
        print("Result =", sub(a,b))
    elif choice == 3:
        print("Result =", mul(a,b))
    elif choice == 4:
        print("Result =", div(a,b))
        
        break  
    else:
        print("Invalid, choose a number from 1-4")
