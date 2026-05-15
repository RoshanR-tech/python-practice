#Default Arguments
def student(name , course="python"):             #default of course would be python until it is changed 
    print(f"Hello {name} is learning {course}")
student("Roshan.R")
student("ankit","java")

#keyword arguments
def student(name , course="Python"):
    print(f"Hello {name} loves {course}")
student("Roshan.R")
student(course="Java",name="Ankith")      #order doesn't matter if it's specified 


# difference btw return and print
#return function 
def sum_return(a,b):
    return a+b

a = int(input("Enter your number: "))   
b = int(input("Enter your number: "))  

result = sum(a,b)
print(result)

# print function 
def sum_print(a,b):
    print(a+b)

a = int(input("Enter your number: "))   
b = int(input("Enter your number: "))  

result = sum(a,b)
print(result)

# Error statement 
# last variables are to be assigned first
def student(name="Roshan.R" , course):
    print(f"{name} is learning {course})
student("vihitha")


def student(name , course="python"):
    print(f"{name} is learning {course}")
    
student("Roshan.R") #default argument (python will be assigned automatically to course)
student(course="Java",name="vihitha") #key word argument (order does not matter if it is directly assigned)
student("vihitha","java") #follows the order 
