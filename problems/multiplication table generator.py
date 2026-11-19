num = int(input("Enter a number: "))

if num < 1:
    print("Invalid input")
else:
    for i in range(1,11):   #range include numbers from 1-10
        print(num,"x",i,"=",num*i)


num = int(input("Enter a number: "))
for i in range(1,11):
    if num < 1 :
        print("Invalid")
    else :
        print(f"{num} x {i} = ",num*i) #better version
