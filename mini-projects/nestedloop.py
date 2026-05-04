#star pattern 
for i in range(1,6):
    for j in range(1,6):
        print("*", end=" ")
    print()


num = int(input("Enter a number: "))
for i in range(1,11):
    print(num, "x", i, "=", num*i)


rows = int(input("Enter rows: "))

for i in range(1, rows+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()


