n = int(input("enter your number: "))
if n < 0 :
    print("it is a negaive number.")
elif n > 0 :
        print("it is a positive number.")
else :
        print("it is a zero.")


n = int(input("enter your number: ")) 
for i in range (1,11):
    print(f"{n} x {i} = {n*i}")


a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
c = int(input("enter your third number: "))
if a>=b and a>=c :
    print(f"{a} is the largest number. ")
elif b >=c :
    print(f"{b} is the largest number. ")
else :
    print(f"{c} is the largest number. ")


total = 0
while True :
    n = int(input("enter your number: "))
    if n == 0 :
        print("executed.")
        break 
    else :
        total += n
print("total number",total)


n = int(input("enter your number: "))
for i in range (1 , n+1):
    print(i)
    
