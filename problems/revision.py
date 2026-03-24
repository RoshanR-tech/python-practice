# Day 8 - Problem 1: Sum of N numbers using accumulator pattern

total = 0

for i in range(1,6):
    total = total + i

print("Sum is:", total)


# Day 8 - Problem 2: Count even numbers using counter pattern

count = 0

for i in range(1,11):
    if i % 2 == 0:
        count = count + 1

print("Total even numbers:", count)


# Day 8 - Problem 3: Print multiplication table

num = 5

for i in range(1,11):
    print(num, "x", i, "=", num*i)

# Day 8 - Problem 4: Increasing number triangle pattern

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

# Day 8 - Problem 5: Reverse star pattern

for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()
