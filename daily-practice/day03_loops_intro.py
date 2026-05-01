#basic conditions using if 
age = int(input("enter your age: "))
if age >= 18 :
    print("you are an adult , eligible to vote ")
else :
    print("you are a minor , Not eligible to vote ")

# senior citizenship  
age = int(input("enter your age: "))
if age >= 60 :
    print("you are a senior citizen ")
elif age >= 18 :
    print("you are an adult ")
else :
    print("you are a minor ")
