#Default Arguments
def student(name , course="python"):
    print(f"Hello {name} is learning {course}")
student("Roshan.R")
student("ankit","java")

#keyword arguments
def student(name , course="Python"):
    print(f"Hello {name} loves {course}")
student("Roshan.R")
student(course="Java",name="Ankith")


# difference btw return and print
#For return
def sum_return(a,b):
    return a+b

a = int(input("Enter your number: "))   
b = int(input("Enter your number: "))  

result = sum(a,b)
print(result)

# For print
def sum_print(a,b):
    print(a+b)

a = int(input("Enter your number: "))   
b = int(input("Enter your number: "))  

result = sum(a,b)
print(result)
