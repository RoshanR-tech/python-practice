for i in range (5 , 0 , -1):   #forms a reverse triangle
    for j in range (i):
        print("*", end=" ")
    print()
    
for i in range (5 , 0 , -1):
    for j in range ( 1 , i+1):
        print(j , end=" ")      #changing numbers
    print()
    
for i in range (5 , 0 , -1):
    for j in range(1 , i+1):
        print(i , end=" ")      #same numbers
    print()
    
num = 1
for i in range (5 , 0 , -1):   #counts from 5 to 1 
    for j in range(1 , i+1):
        print(num , end=" ")    #counting of numbers
        num += 1
    print()
    
for i in range (1, 6):             #logical thinking 
    for j in range (1, i+1):       #logical thinking 
        print(6-j , end=" ")
    print()
