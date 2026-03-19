# problem 1
n = int(input("enter a number: "))
while n != 0 :
    print(n)
    n = int(input("next:"))
if n == 0:
    print("completed")

# problem 2
    while True :
     n = int(input("enter your number:"))
     if n < 0:
        print("invalid")
        break
    
    if n%2==0 :
        print("even")
    else :
        print("odd")


# problem 3
for i in range (1, 20) :
    if i%2==0 :
        print (f"even{i}")
    else :
        print(f"odd{i}")

#problem 4
even_count = 0
odd_count = 0
for i in range(1 , 21):
    if i%2==0 :
        even_count = even_count+1
    else :
        odd_count = odd_count+1
        
print(even_count)
print(odd_count)


#day 6 challenge 
divisable_by_5 = 0
for i in range (1 , 51):
    if i%5==0 :
        divisable_by_5 = divisable_by_5 + 1
print(f"total number divisible by 5 : {divisable_by_5}")    
        

#problem 5
correct = 1234
while True :
    password = int(input("enter your number: "))
    if correct == password :
        print("access granted")
        break 
    else :
        print("wrong password")


#problem 6
count = 0 
while True :
    n = int(input("enter your number :"))
    if n== 0:
       break 
    count = count + 1 
print("total number:", count)


 #problem 7
total = 0 
while True :
    n = int(input("enter your number :"))
    if n== 0:
       break 
    total = total + n 
print("total number:", total)

               
#problem 8
while True:
 n = int(input("enter your number: "))
 if n==  0:
  print("bye")
  break
else :
  print("hello")
