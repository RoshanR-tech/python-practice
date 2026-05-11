#Discount system
num_items = int(input("Number of items : "))
total= 0 
for i in range (num_items):
    price = float(input(f"Enter the price of your item :"))
    total += price 

print ("Total amount before discount : ",total)

if total < 999 :  #discount logic
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
