seceret_number = 6769
while True :
    number = int(input("enter your guess :"))
    if number == seceret_number :
        print("correct guess")
        break
    else :
     print("wrong guess")