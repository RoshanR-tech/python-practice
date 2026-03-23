for i in range (5 , 0 , -1):
    for j in range (i):
        print("*", end=" ")
    print()
    
for i in range (5 , 0 , -1):
    for j in range ( 1 , i+1):
        print(j , end=" ")
    print()
    
for i in range (5 , 0 , -1):
    for j in range(1 , i+1):
        print(i , end=" ")
    print()
    
num = 1
for i in range (5 , 0 , -1):
    for j in range(1 , i+1):
        print(num , end=" ")
        num += 1
    print()
    
for i in range (1, 6):        #logical thinking 
    for j in range (1, i+1):
        print(6-j , end=" ")
    print()
