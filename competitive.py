#Discount system
num_items = int(input("Number of items : "))
total= 0 
for i in range (num_items):
    price = float(input(f"Enter the price of your item :"))
    total += price 

print ("Amount before discount : ",total)

if total < 1000 :  #discount logic
    discount = 0
elif total >= 1000 and total <= 5000 :   
    discount = total * 0.10 
elif total >= 5000 and total <= 10000 :
    discount = total*0.20 
elif total >= 10000 :
    discount = total*0.25 + 500 
    
final_amount = total - discount 
print("Total amount after discount : ",final_amount) #f string can also be incuded 
    

#fixed discount along with additional offers
#discount on item and discount based on the price of the bill
def calculate_final_cost(items):
subtotal = 0
for price, discount_percent in items:
item_cost = price – (price * discount_percent / 100)
subtotal += item_cost
percentage_discount = 0
fixed_discount = 0
if subtotal > 500:
percentage_discount = subtotal * 0.10
if subtotal > 1000:
fixed_discount = 150
discount = max(percentage_discount, fixed_discount)
final_cost = subtotal – discount
return int(final_cost)
n = int(input())  #input
items = [tuple(map(int, input().split())) for _ in range(n)]
print(calculate_final_cost(items))



#large number modula 
# Input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
# Compute sum modulo
total = 0
for num in arr:
 total = (total + num) % m
print(total)



#Modular Exponentiation
def mod_exp(a, m, p):
result = 1
a = a % p # reduce a initially
while m > 0:
 if m % 2 == 1: # if m is odd
 result = (result * a) % p
 a = (a * a) % p # square a
 m = m // 2
 return result
# Input
a, m, p = map(int, input().split())
print(mod_exp(a, m, p))
