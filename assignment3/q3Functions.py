#Problem 3

def perfect(n):
    count = 2
    total = 1
    while(count < n/count):
        if(n/count == round(n/count)):
            total += count + n/count
        
        count += 1
    
    if(count == n/count):
        total += count

    if(total == n):
        print(n, "is a perfect number")
    else:
        print(n, "is not a perfect number")
    
nums = [6, 2, 20, 496, 30, 8128, 500, 1000, 33550336, 999983]

for i in range(0,len(nums)):
    perfect(nums[i])