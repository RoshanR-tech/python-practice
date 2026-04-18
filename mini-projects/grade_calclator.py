total = 0     #initial values  
count = 0     

while True:
    marks = int(input("Enter marks (-1 to stop): "))    #cannot be negative 

    if marks == -1:
        break

    if marks < 0 or marks > 100:
        print("Invalid marks")
        break

    total = total + marks
    count = count + 1

if count == 0:
    print("No marks entered")
else:
    average = total / count

    print("Total marks =", total)
    print("Subjects =", count)
    print("Average =", average)

    if average >= 90:
        print("Grade: A")
    elif average >= 75:
        print("Grade: B")
    elif average >= 50:
        print("Grade: C")
    else:
        print("Grade: Fail")
