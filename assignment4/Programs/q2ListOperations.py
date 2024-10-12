#Problem 2-a
print("\nq2 part a\n")

a = eval(input("q2 part a input (list):"))

mean = sum(a)/len(a)

l = []
for i in a:
    last = True
    for j in range(0,len(l)):
        if(abs(i - mean) < abs(l[j] - mean)):
            l.insert(j, i)
            last = False
            break
        elif(abs(i - mean) < abs(l[j] - mean)):
            if(i < l[j]):
                l.insert(j, i)
            else:
                l.insert(j+1, i)
    if(last):
        l.append(i)
            
a = l

print(a)

#Problem 2-b
print("\n\nq2 part b\n")

def rotate(l,k):
    k = k%len(l)
    return l[k:] + l[:k]

k = int(input("q2 part b input (integer):"))
nums = [1,2,3,4,5]

print("function input:", nums, ",", k)
print(rotate(nums,k))

#Program 2-c
print("\n\nq2 part c\n")

def cumulative(l):
    for i in range(1,len(l)):
        l[i] *= l[i-1]
    return l

nums = [1,2,3,4]

print("function input:", nums)
print(cumulative(nums))

#Problem 2-d
print("\n\nq2 part d\n")

k = 10
nums = [10,20,10,30,10]
index = []

for i in range(0,len(nums)):
    if(nums[i] == k):
        index.append(i)

print("list:", nums, "and k:", k)
print(index)

print("\n\n")