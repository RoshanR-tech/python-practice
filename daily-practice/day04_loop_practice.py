marks = int(input("enter your marks: "))

if marks < 0 or marks > 100:
    print("invalid")
else:
    print("valid")

    if marks >= 90:
        print("A grade")
    elif marks >= 75:
        print("B grade")
    elif marks >= 50:
        print("C grade")
    else:
        print("F grade")

    if marks >= 50:
        print("you passed")
    else:
        print("you failed")
