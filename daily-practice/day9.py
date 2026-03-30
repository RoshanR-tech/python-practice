# for fixed patter
def pattern():
    for i in range(2):
        for j in range(6):
            print("*", end=" ")
        print()

pattern()

# increasing triangle
def pattern():
    for i in range (1,4):
        for j in range (1, i+1):
            print ("*", end=" ")
        print()
pattern()

# To print stars in 4 rows and columns 
def pattern():
    for i in range (4):
        for j in range (4):
            print ("*", end=" ")
        print()
pattern()


#function to greet user
def greeting(name):
    print("Hello",name)
greeting("Roshan")
greeting("Vihitha")


# input can be given while calling the function 
# Function to calculate rectangle area
def rectangle_area(length, width):
    print("Area is", length * width)

rectangle_area(5, 4)


# Function to print square pattern
def square_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

square_pattern(3)


# Return vs Print
def square(n):
    return n*n
n = int(input("enter your number: "))   
result = square(n)
print("square is" , result)

def square(n):
    print(n*n)
n = int(input("enter your number: "))   
result = square(n)
print("square is" , result)


# Add using return
def add(a,b):
    return a+b 
    
result = add(10,5)
print("sum is", result )


