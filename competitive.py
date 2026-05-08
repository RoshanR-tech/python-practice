#Discount system
num_items = int(input("Number of items : "))
total= 0 
for i in range (num_items):
    price = float(input(f"Enter the price of your item :"))
    total += price 

print ("Total amount before discount : ",total)

if total < 1000 :
    discount = 0
elif total >= 1000 and total <= 5000 :
    discount = total * 0.10 
elif total >= 5000 and total <= 10000 :
    discount = total*0.20 
elif total >= 10000 :
    discount = total*0.25 + 500 
    
final_amount = total - discount 
print("Total amount after discount : ",final_amount)
    
