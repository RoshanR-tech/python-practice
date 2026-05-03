#star pattern
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()


for i in range(5, 0 , -1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()


for i in range(1, 6): #the outer loop runs 5 times
    for j in range(1):
        print("*", end=" ")
   

for i in range(1):     #the inner loop runs 5 times 
   for j in range(1, 6):
        print("*", end=" ")
   

for i in range(1,6):        # controls rows
    for j in range(i):     # controls stars (increasing)
        print("*", end=" ")
    print()                # move to next row



for i in range(1,6):        # reverse triangle 
    for j in range(6-i):    
        print("*", end=" ")
    print()                


for i in range(1,6):        
    for j in range(1, i+1):    
        print( j, end=" ")
    print()                


for i in range(1,6):          # controls rows
    for j in range(i):        # controls how many numbers per row
        print(i, end=" ")     # print the row number
    print()                   # move to next line
