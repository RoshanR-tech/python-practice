# ==========================================
# Day 8 – Pattern Logic and Loop Control
# Python Learning Journey
# Topics covered:
# 1. Nested pattern logic
# 2. Row vs column printing (i vs j)
# 3. Multiplication and addition patterns
# 4. break statement
# 5. continue statement
# ==========================================


# Pattern 1 – Row numbers square
for i in range(1,6):
    for j in range(1,6):
        print(i, end=" ")
    print()


print()   # space between patterns


# Pattern 2 – Column numbers square
for i in range(1,6):
    for j in range(1,6):
        print(j, end=" ")
    print()


print()


# Pattern 3 – Increasing number triangle (j controls values)
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()


print()


# Pattern 4 – Increasing triangle (i controls values)
for i in range(1,6):
    for j in range(1,i+1):
        print(i, end=" ")
    print()


print()


# Pattern 5 – Square star pattern
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()


print()


# Pattern 6 – Reverse star triangle
for i in range(5):
    for j in range(5-i):
        print("*", end=" ")
    print()


print()


# Pattern 7 – Multiplication triangle
for i in range(1,6):
    for j in range(1,i+1):
        print(i*j, end=" ")
    print()


print()


# Pattern 8 – Addition triangle
for i in range(1,6):
    for j in range(1,i+1):
        print(i+j, end=" ")
    print()


print()


# Example 1 – break statement
for i in range(1,10):
    if i == 5:
        break
    print(i)


print()


# Example 2 – continue statement
for i in range(1,6):
    if i == 3:
        continue
    print(i)


print()


# Example 3 – break and continue combined
for i in range(1,8):
    if i == 4:
        continue
    if i == 6:
        break
    print(i)


# Author: Roshan R
# Course: Python Fundamentals
# Day: 8
# Description: Pattern problems and loop control practice
