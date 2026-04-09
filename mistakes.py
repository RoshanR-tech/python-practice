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





# ==========================================
# MISTAKE 1 : Forgetting to call the function
# ==========================================

def greet():
    print("Hello")

# Mistake :
# Function was created but never called.
# So no output appears.

# Fix :
greet()



# ==========================================
# MISTAKE 2 : Using print instead of return
# ==========================================

def add(a,b):
    print(a+b)

result = add(5,3)

# Mistake :
# Function used print instead of return.
# So result becomes None.

print(result)   # Output : None

# Fix :

def add(a,b):
    return a+b

result = add(5,3)
print(result)



# ==========================================
# MISTAKE 3 : Getting None in output
# ==========================================

def square(n):
    print(n*n)

print(square(4))

# Mistake :
# Function prints value but does not return it.
# So Python prints None after execution.

# Fix :

def square(n):
    return n*n

print(square(4))



# ==========================================
# MISTAKE 4 : Wrong use of range ending value
# ==========================================

for i in range(1,5):
    print(i)

# Mistake :
# Expected output till 5.
# But range stops before the end value.

# Output :
# 1 2 3 4

# Fix :

for i in range(1,6):
    print(i)



# ==========================================
# MISTAKE 5 : Wrong range step understanding
# ==========================================

for i in range(1,10,2):
    print(i)

# Mistake :
# Thinking it prints every number.
# But step 2 skips numbers.

# Output :
# 1 3 5 7 9



# ==========================================
# MISTAKE 6 : Using range without loop
# ==========================================

range(5)

# Mistake :
# range alone does nothing.
# Must be used inside loop or converted.

# Fix :

for i in range(5):
    print(i)



# ==========================================
# MISTAKE 7 : Parameter mismatch
# ==========================================

def multiply(a,b):
    return a*b

multiply(5)

# Mistake :
# Function expects 2 arguments but only 1 given.
# Causes error.

# Fix :

multiply(5,2)



# ==========================================
# MISTAKE 8 : Local variable confusion
# ==========================================

def test():
    x = 10

print(x)

# Mistake :
# x is local to function.
# Cannot access outside.

# Fix :

def test():
    x = 10
    return x

print(test())



# ==========================================
# MISTAKE 9 : Using return and print together wrongly
# ==========================================

def number():
    return 5
    print("Hello")

# Mistake :
# Code after return never executes.

# Fix :

def number():
    print("Hello")
    return 5



# ==========================================
# MISTAKE 10 : Wrong loop inside function indentation
# ==========================================

def show():
for i in range(5):
    print(i)

# Mistake :
# Indentation error.
# Loop must be inside function.

# Fix :

def show():
    for i in range(5):
        print(i)

show()



# ==========================================
# MISTAKE 11 : Confusing range start and stop
# ==========================================

for i in range(5):
    print(i)

# Mistake :
# Thinking it prints 1 to 5.
# Actually prints 0 to 4.

# Fix :

for i in range(1,6):
    print(i)



# ==========================================
# MISTAKE 12 : Function not returning calculated value
# ==========================================

def average(a,b):
    total = a+b
    avg = total/2

# Mistake :
# Forgot return statement.

print(average(4,6))   # Output None

# Fix :

def average(a,b):
    total = a+b
    avg = total/2
    return avg

print(average(4,6))






# ============================================
# DAY 10 – MISTAKE MONITORING (FUNCTIONS)
# Tracking mistakes I made while learning functions
# ============================================


# ============================================
# Mistake 1: Expecting output without calling function
# ============================================

# Mistake I did:
def add(a,b):
    print(a+b)

# I expected output here without calling function


# Why it happened:
# Function only runs when it is called.


# Solution:
# Call the function

add(5,3)



# ============================================
# Mistake 2: Confusion between print and return
# ============================================

# Mistake I did:

def sum(a,b):
    print(a+b)

result = sum(4,6)

print(result)

# Output showed None


# Why it happened:
# Print only displays value.
# It does not send value back.


# Solution:
# Use return instead of print.

def sum(a,b):
    return a+b

result = sum(4,6)

print(result)



# ============================================
# Mistake 3: Function returning None
# ============================================

# Mistake I did:

def test():
    print("Hello")

value = test()

print(value)


# Why it happened:
# If return is not written, python automatically returns None.


# Solution:
# Only store function if it returns something.

def test():
    return "Hello"

value = test()

print(value)



# ============================================
# Mistake 4: Not understanding global variable usage
# ============================================

# Mistake I did:

x = 10

def change():
    x = 20

change()

print(x)


# Why it happened:
# Python created a local variable instead of changing global.


# Solution:
# Use global keyword.

x = 10

def change():
    global x
    x = 20

change()

print(x)



# ============================================
# Mistake 5: Confusion between lambda and normal function
# ============================================

# What I thought:
# Lambda can replace every function.


# What I learned:
# Lambda is only good for small one line expressions.
# Normal functions are better for complex logic.


# Example:

square = lambda x : x*x

print(square(5))


def square2(x):
    return x*x

print(square2(5))



# ============================================
# KEY LEARNINGS FROM TODAY
# ============================================

# 1 Functions only work when called
# 2 Print shows value, return sends value back
# 3 Functions return None if return is missing
# 4 Global keyword modifies global variable
# 5 Lambda is for short functions only


# ============================================
# PERSONAL NOTE:
# I should focus more on understanding return vs print
# because most of my mistakes came from this confusion.
# ============================================
