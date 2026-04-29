#increase the number 
n = 1 
while n<=5:
    print(n)
    n = n+1 

#decrease the number 
n = 5 
while n>=1:
    print(n)
    n = n-1 

#rectangular star pattern 
for i in range (1,5):
    for j in range(1,i+1):
        print("*" , end=" ")
    print()


#reverse star pattern
for i in range (6,0,-1):
    for j in range(1,i+1):
        print("*" , end=" ")
    print()
