#creating a list of numbers
nums = [10,20,30,40,50] 
print(nums[0])
print(nums[-1])
nums[2]=100
print(nums)

#list methods
nums = [1,2,3]
nums.append(4)
nums.insert(1 , 10) #nums.insert(index , value)
nums.remove(2)
nums.pop(-1) #automatically removs last element but still using -1 just for better understanding
print(nums)

#using for loop 
total = 0 
nums = [5,10,15,20]
for num in nums :
    print(num)
    total = total + num 

print(total)
