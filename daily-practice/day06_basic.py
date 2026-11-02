#basic even function while loop 
n = 1 
while n <= 10 :
    if n%2==0:
        print(n)
    n = n+1


#same logic 
n = 1 
while n < 10 :
    if n%2!=0:
        print(n)
    n = n+1


n = 5 
while n > 0 :
    print(n)
    n -= 1 
print("lift off") #counting backwards // counting in reverse 


pas = "Rossi@123"
while True :
    password = input("Enter your password : ")
    if password == pas :
        print("Access granted.")
        break 
    
    else :
        print("Access denied.")
    

n = 1 
total = 0 
while n <= 5 :
    total += n 
    n += 1
    
print(total)
    

se = 7 
while True :
    Secret = int(input("Enter your Secret number : "))
    if Secret == se :
        print("You got it! Lucky 7!")
        break 
    
    else :
        print("Wrong guess, try again!")
