n = int(input("enter your number: "))
if n < 0 :
    print("it is a negaive number.")
elif n > 0 :
        print("it is a positive number.")
else :
        print("it is a zero.")


n = int(input("enter your number: ")) 
for i in range (1,11):
    print(f"{n} x {i} = {n*i}")


a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
c = int(input("enter your third number: "))
if a>=b and a>=c :
    print(f"{a} is the largest number. ")
elif b >=c :
    print(f"{b} is the largest number. ")
else :
    print(f"{c} is the largest number. ")


total = 0
while True :
    n = int(input("enter your number: "))
    if n == 0 :
        print("executed.")
        break 
    else :
        total += n
print("total number",total)


n = int(input("enter your number: "))
for i in range (1 , n+1):
    print(i)
    



# ==========================================
# MENU DRIVEN PROGRAMS COLLECTION
# Author: Roshan R
# Concepts used: loops, functions, conditionals, strings
# ==========================================


# ==========================================
# PROGRAM 1 : MENU DRIVEN CALCULATOR
# ==========================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


while True:

    print("\n--- Calculator Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        break

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(num1, num2))

    elif choice == 2:
        print("Result:", subtract(num1, num2))

    elif choice == 3:
        print("Result:", multiply(num1, num2))

    elif choice == 4:
        print("Result:", divide(num1, num2))

    else:
        print("Invalid choice")



# ==========================================
# PROGRAM 2 : NUMBER UTILITY PROGRAM
# ==========================================

def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


def factorial(n):

    fact = 1

    for i in range(1, n+1):
        fact = fact * i

    return fact


def reverse_number(n):

    rev = 0

    while n > 0:

        digit = n % 10

        rev = rev * 10 + digit

        n = n // 10

    return rev



while True:

    print("\n--- Number Utility Menu ---")
    print("1 Even or Odd")
    print("2 Factorial")
    print("3 Reverse Number")
    print("4 Exit")

    choice = int(input("Enter choice: "))

    if choice == 4:
        break

    num = int(input("Enter number: "))


    if choice == 1:
        print(even_or_odd(num))

    elif choice == 2:
        print("Factorial:", factorial(num))

    elif choice == 3:
        print("Reverse:", reverse_number(num))

    else:
        print("Invalid choice")



# ==========================================
# PROGRAM 3 : STRING OPERATIONS MENU
# ==========================================

def count_vowels(text):

    vowels = "aeiouAEIOU"

    count = 0

    for char in text:

        if char in vowels:

            count = count + 1

    return count



def reverse_string(text):

    return text[::-1]



def palindrome(text):

    if text == text[::-1]:

        return "Palindrome"

    else:

        return "Not Palindrome"



while True:

    print("\n--- String Menu ---")
    print("1 Count vowels")
    print("2 Reverse string")
    print("3 Palindrome check")
    print("4 Exit")

    choice = int(input("Enter choice: "))

    if choice == 4:
        break

    text = input("Enter string: ")


    if choice == 1:

        print("Vowels:", count_vowels(text))


    elif choice == 2:

        print("Reverse:", reverse_string(text))


    elif choice == 3:

        print(palindrome(text))


    else:

        print("Invalid choice")



# ==========================================
# PROGRAM 4 : SIMPLE BANK SYSTEM
# ==========================================

balance = 0

while True:

    print("\n--- Bank Menu ---")

    print("1 Deposit")

    print("2 Withdraw")

    print("3 Check Balance")

    print("4 Exit")


    choice = int(input("Enter choice: "))


    if choice == 1:

        amount = int(input("Enter amount: "))

        balance = balance + amount

        print("Balance:", balance)



    elif choice == 2:

        amount = int(input("Enter amount: "))

        if amount > balance:

            print("Insufficient balance")

        else:

            balance = balance - amount

            print("Balance:", balance)



    elif choice == 3:

        print("Current Balance:", balance)



    elif choice == 4:

        break



    else:

        print("Invalid choice")
