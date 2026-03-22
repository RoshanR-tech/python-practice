for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()


for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()


for i in range(1,6):
    for j in range(i,6):
        print("*", end=" ")
    print()


for i in range(1,6):
    for j in range(1,6):
        print("*", end=" ")
    print()


for i in range(1,6):                 # Increasing number triangle (controls rows)
    for j in range(1 , i+1):         # Prints numbers from 1 to i
        print(j , end=" ")           # Print column number (j)
    print()                          # Move to next row

for i in range(5,0,-1):              # Decreasing number triangle (rows from 5 to 1)
    for j in range(1 , i+1):         # Prints number i, i times
        print(i , end=" ")           # Print row number (i)
    print()                          # Move to next row
