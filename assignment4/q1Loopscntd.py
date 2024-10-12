#Problem 1-a
print("\nq1 part a\n")

def primelist(n):
    l = [2]
    
    for i in range(3,n+1,2):
        isprime = True
        j = 0
        sqrt = i**0.5
        while(l[j] <= sqrt):
            if(i%l[j] == 0):
                isprime = False
                break
            j += 1
        if(isprime):
            l.append(i)
        
    return l

num = int(input("q1 part a input (integer):"))

print(primelist(num))

#Problem 1-b
print("\n\nq1 part b\n")

def listcount(l):
    
    if(l == []):
        return -1
    
    new = []
    
    while(len(l) > 0):
        count = 0
        topop = []
        for j in range(0,len(l)):
            if(l[j] == l[0]):
                count += 1
                topop.append(j)
                
        new.append([l[0],count])
        
        for i in range(0,len(topop)):
            l.pop(topop[i] - i)
    
    return new

nums = [1,2,3,1,1,2,1,1]

print("function input:", nums)
print(listcount(nums))

#Problem 1-c
print("\n\nq3 part c\n")

def findpair(l,t):
    for i in l:
        for j in l:
            if(i+j == t):
                return (i,j)
    return -1

nums = [2,4,3,5,7]
target = 9

print("function input:", nums,",", target)
print(findpair(nums,target))

print("\n\n")