while True :
    print("\nmenu")
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
    
