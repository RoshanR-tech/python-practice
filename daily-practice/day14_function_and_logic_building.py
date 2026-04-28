#logic building
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
n = int(input("Enter a number: "))

def is_even(n):
    return n % 2 == 0

def is_positive(n):
    return n > 0

def check_number(n):
    if is_positive(n):
        if is_even(n):
            print("Positive Even")
        else:
            print("Positive Odd")
    else:
        if is_even(n):
            print("Negative Even")
        else:
            print("Negative Odd")

check_number(n)
