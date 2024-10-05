xlist=[]
N=int(input("enter the value of N:"))
for i in range(N):
    x=input(f"enter the value of x-{(i+1)}:")
    xlist.append(float(x))


xlist.sort()
n=len(xlist)
if n%2==1:
    median=xlist[((n+1)//2)-1]
else:
    median=((xlist[(n//2)-1])+(xlist[((n+2)//2)-1]))/2

xlist.append(median)
sumlist=[]
def sumlistcaller(k):
    sum0=0
    for i in range(len(xlist)):
        sum0+=abs((xlist[k]-xlist[i]))
    sumlist.append(sum0)


for j in range(len(xlist)):
    sumlistcaller(j)


finallist=[]

for z in range(len(xlist)):
    finallist.append([xlist[z],sumlist[z]])

print(finallist)


for c in range(len(xlist)):
    print(f"the value of S for x-{c+1} is: {finallist[c][1]}")
print(f"x-{len(xlist)} is the median and we can see the minimum value of S comes at the median.")
