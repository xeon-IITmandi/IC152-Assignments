xlist=[]
N=int(input("enter the value of N:"))
for i in range(N):
    x=input(f"enter the value of x-{(i+1)}:")
    xlist.append(float(x))

sum=0
for num in xlist:
    sum+=num
avg=sum/len(xlist)#float value

xlist.append(avg)

sumlist=[]
def sumlistcaller(k):
    sum0=0
    for i in range(len(xlist)):
        sum0+=(xlist[k]-xlist[i])**2
    sumlist.append(sum0)


for j in range(len(xlist)):
    sumlistcaller(j)

# print(sumlist)

finallist=[]

for z in range(len(xlist)):
    finallist.append([xlist[z],sumlist[z]])

print(finallist)


for c in range(len(xlist)):
    print(f"the value of S for x-{c+1} is: {finallist[c][1]}")
print(f"x-{len(xlist)} is the mean and we can see the minimum value of S comes at the mean.")











