#normal function
def add(a,b):
    return a+b
#lambda function
add = lambda a,b : a+b


#lambda functions
cube = lambda n : n*n*n
subtract = lambda a,b : a-b
is_even = lambda n : n%2==0 
print(cube(3))
print(subtract(2,3))
print(is_even(2))



#multiple functions
def multiplication(a,b):
    return a*b

def greater(a,b):
    if a>b :
        return a
    else :
        return b 
        
def is_positive(n):
    if n > 0 :
        return "True"
    else :
        return "False"
        
print(multiplication(2,3))
print(greater(2,3))
print(is_positive(3))
