while True :
    print("\nmenu") #automatically creates a new line 
    print("1. print numbers from 1-10")
    print("2. even odd checker")
    print("3.exit")
    
    choice = int(input("enter your option: "))
    
    if choice == 1:
        for i in range(1,11):
            print(i)
    
    elif choice == 2 :
        n=int(input("enter your number: "))
        if n%2==0:
            print("even number")
        else :
            print("odd number")
            
    elif choice == 3 :
        print("exiting the program........")
        break 
    
    else :
        print("invalid")


#menu driven program 2
while True :
    print("\nMenu") 
    print("1. range function")
    print("2. sum of n numbers")
    print("3. sign checker")
    print("4. multiplication table")
    print("5. counter")
    print("6. largest of 3 numbers")
     
    choice = int(input("select a number from the menu : "))
    
    if choice == 1:
        n = int(input("enter your number: "))
        for i in range (1 , n+1 ):
           print(i)
           
    if choice == 2:
        total = 0 
        n = int(input("enter your number: ")) 
        
        while n != 0:
            total += n
            n = int(input("next: ")) 
            
        print("sum is", total)
        
        
    if choice == 3 :
        n = int(input("enter your number: "))
        if n < 0 :
            print("it is a negaive number.")
        elif n > 0 :
            print("it is a positive number.")
        else :
            print("it is a zero.")
            
            
    if choice == 4 :
        n = int(input("enter your number: "))
        for i in range (1,11):
           print(f"{n} x {i} = {n*i}")
           
           
    if choice == 5:
        count = 0
        while True:
            n = int(input("enter your number: "))
            if n == 0:
                print("executed.")
                break 
            else:
                count += 1
        
        
        print("total numbers entered:", count)
        
        
        
    if choice == 6:
        a = int(input("enter your first number: ")) 
        b = int(input("enter your second number: "))
        c = int(input("enter your third number: "))
        
        if a >= b and a >= c:
            print(f"{a} is the largest number.")
        elif b >= c:
            print(f"{b} is the largest number.")
        else:
            print(f"{c} is the largest number.")
