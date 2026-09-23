num = int(input("Enter a number: "))

if num < 1:
    print("Invalid input")
else:
    for i in range(1,10):
        print(num,"x",i,"=",num*i)
