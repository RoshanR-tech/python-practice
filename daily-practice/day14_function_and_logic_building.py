#logic building using functions
#Basic logic building
n = int(input("Enter a numer : "))
def is_even(n):
    if n%2==0 :
        print("Yes it is Even")
        return True
    else :
        print("Yes it is Odd")
        return False
result = is_even(n)
print(result)

def is_positive(n):
    if n > 0 :
        print("Yes it a positive number")
        return True
    else :
        print("No it a negative number")
        return False
result = is_positive(n)
print(result)

def check_number(n):
    if n > 0 and n%2==0 :
        print ("positive even")
    elif n > 0 and n%2!=0 :
        print("positive odd")
    elif n < 0 and n%2 == 0 :
        print("negative even")
    else :
        print("negative odd")
result = check_number(n)
print(result)


#better version of the above code
n = int(input("Enter a number : "))

def is_even(n):
    return n%2 == 0  
    
def is_positive(n):
    return n > 0
    
def check_number(n):
    if is_positive(n):
        if is_even(n):
            print("positive even num")
        else :
            print("positive num")
    else :
        if is_even(n):
            print("negative even num")
        else :
            print("negative odd num")

check_number(n)


#print vs return logic building 
n = int(input("Enter a number : "))

def calculate_square(n):
    return n*n
    
def calculate_cube(n):
    return n*n*n
    
def check_number_type(n):
    if n%2==0 :
        return calculate_square(n)
    else :
        return calculate_cube(n)
        
print(check_number_type(n))



#divisibility logic 
n = int(input("Enter a number : "))

def is_divisible_by_3(n):
    return n % 3 == 0
        
def is_divisible_by_5(n):
    return n % 5 == 0 
        
def check_divisibility(n):
    if is_divisible_by_3(n) and is_divisible_by_5(n):
        print("divisible by 3 and 5.")
        
    elif is_divisible_by_3(n):
        print("divisible by 3.")
      
    elif is_divisible_by_5(n):
        print("divisible by 3.")
        
    else : 
        print("divisible by none. ")
        
        
check_divisibility(n)



#complex structure 
n = int(input("Enter a number: "))

def is_positive(n):
    return n > 0

def is_even(n):
    return n % 2 == 0

def get_number_type(n):
    if is_positive(n):
        return "Positive"
    else:
        return "Negative"

def calculate_square(n):
    return n * n

def calculate_cube(n):
    return n * n * n

def process_number(n):
    if get_number_type(n) == "Positive":
        if is_even(n):
            print(calculate_square(n))
        else:
            print(calculate_cube(n))
    else:
        if is_even(n):
            print(abs(n))
        else:
            print("Invalid input")

process_number(n)
