# Simple Calculator using Functions
# Day 9 Mini Project
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

if __name__ == "__main__":
    print("\n----MENU----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. division")

choice = int(input("Select a function: "))

    
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

if choice == 1:
    result = add(a,b)
    print(f"Addition of the numbers {a} and {b} is: ",result)

elif choice == 2:
    result = sub(a,b)
    print(f"Subtraction of the numbers {a} and {b} is: ",result)
    
elif choice == 3:
    result = mul(a,b)
    print(f"multiplication of the numbers {a} and {b} is: ",result)
    
elif choice == 4:
    if b == 0:
        print("cannot be divided. ")
    else: 
        result = div(a,b)
        print(f"division of the numbers {a} and {b} is: ",result)
    
else :
    print("Invalid option .Please choose a numbers from 1-4")

    

