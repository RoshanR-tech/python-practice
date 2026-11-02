#increase the number 
n = 1 
while n<=5:   #range 
    print(n)
    n = n+1 

#decrease the number 
n = 5 
while n>=1:
    print(n)
    n = n-1 

#triangular star pattern 
for i in range (1,5):
    for j in range(1,i+1):
        print("*" , end=" ")
    print()


#reverse triangular star pattern
for i in range (6,0,-1):
    for j in range(1,i+1):
        print("*" , end=" ")
    print()


#square star pattern
for i in range (1,5):
    for j in range(i):
        print("*" , end=" ")
    print()


for i in range(20,0,-1):
    if i%4==0 :
        print(i)   #for loop 
        
        
num = 20
while num > 0 :
    if num%4==0:
        print(num)
    num -= 1     #same code as above but using while loop 
