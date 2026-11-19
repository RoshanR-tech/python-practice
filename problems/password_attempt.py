#password system
correct_password = "python@12345"
attempts = 0
max_attempts = 10

while attempts < max_attempts:

    password = input("Enter your  password: ")

    if password == correct_password:
        print("Access Granted")
        break

    else:
        attempts = attempts + 1

        if attempts == max_attempts:
            print("Account Locked")
        else:
            print("Thats the wrong password")
            print("Attempts left:", max_attempts - attempts)


password = "Apple@123"
count = 0 
while count < 5 :
    key = input("Enter your password: ")
    if key == password :
        print("access granted.")
        break 
    else :
        print("Try again.")
    count+=1
print("Attempt limit exceeded.")  #better version 
        
    
