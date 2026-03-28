# Mistake 1 – Confusion between i and j in nested loops

for i in range(3):
    for j in range(3):
        print(i, end=" ")   # Mistake: printing i instead of j
    print()

# Fix
for i in range(3):
    for j in range(3):
        print(j, end=" ")
    print()

# Lesson:
# i controls rows
# j controls columns


# Mistake 2 – Counter printed inside loop instead of after loop

count = 0

for i in range(1,6):
    count = count + 1
    print(count)   # Mistake: printing inside loop

# Fix
count = 0

for i in range(1,6):
    count = count + 1

print(count)

# Lesson:
# Print counter outside loop if total count is needed



# Mistake 3 – Pattern printing going to next line

for i in range(3):
    for j in range(3):
        print("*")   # Mistake: goes to next line

# Fix
for i in range(3):
    for j in range(3):
        print("*", end="")
    print()

# Lesson:
# Use end="" to print in same line

# Mistake 4 – Forgetting i+1 in pattern questions

for i in range(5):
    print("*" * i)   # Mistake: first line empty

# Fix
for i in range(5):
    print("*" * (i+1))

# Lesson:
# Use i+1 when pattern should start from 1



# Mistake 5 – Infinite loop by forgetting increment

i = 1

while i <= 5:
    print(i)
    # Mistake: forgot i = i + 1

# Fix
i = 1

while i <= 5:
    print(i)
    i = i + 1

# Lesson:
# Always update loop variable


# Mistake 6 – Wrong position of print in number patterns

for i in range(1,4):
    for j in range(1,4):
        print(j)
    # Mistake: missing end=""
    print()

# Fix
for i in range(1,4):
    for j in range(1,4):
        print(j, end=" ")
    print()

# Lesson:
# end="" controls horizontal printing


# Mistake 7 – Accumulator not updating

total = 0

for i in range(1,6):
    total + i   # Mistake: value not stored

print(total)

# Fix
total = 0

for i in range(1,6):
    total = total + i

print(total)

# Lesson:
# Always store updated value



# Mistake 8 – Wrong range value

for i in range(1,5):
    print(i)   # Mistake: expected till 5 but stops at 4

# Fix
for i in range(1,6):
    print(i)

# Lesson:
# Range excludes last value


