#password system
correct_password = "python@123"
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
