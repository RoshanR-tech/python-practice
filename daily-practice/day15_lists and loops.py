#basic list and loops code 
numbers = []              #creates a list 
for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)
total = 0
for num in numbers:
    total += num        #adding 
max_num = numbers[0]
for num in numbers:
    if num > max_num:   #maximum
        max_num = num
min_num = numbers[0]
for num in numbers:
    if num < min_num:    #minimum
        min_num = num
print("List:", numbers)
print("Sum:", total)
print("Max:", max_num)
print("Min:", min_num)


