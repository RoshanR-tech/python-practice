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


# Day 8 - Problem 6: Prime number checker

num = int(input("Enter a number: "))

count = 0

for i in range(1, num+1):
    if num % i == 0:
        count = count + 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")


# Day 8 - Problem 7: Sum of digits using while loop

num = int(input("Enter number: "))

total = 0

while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10

print("Sum of digits:", total)


# Day 8 - Problem 8: Reverse a number

num = int(input("Enter number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse*10 + digit
    num = num // 10

print("Reversed number:", reverse)

# Day 8 - Problem 9: Number guessing game

secret = 7

while True:

    guess = int(input("Guess the number: "))

    if guess == secret:
        print("Correct guess!")
        break

    elif guess > secret:
        print("Too high")

    else:
        print("Too low")


# Day 8 - Problem 10: Fibonacci series

n = 10

a = 0
b = 1

for i in range(n):

    print(a)

    c = a + b
    a = b
    b = c


