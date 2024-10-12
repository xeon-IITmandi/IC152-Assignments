numlist=[]
for i in range(10):
    x=float(input(f"enter no. {i+1}:"))
    numlist.append(x)

numlist.sort()
n=len(numlist)
if n%2==1:
    print(f"the median is {numlist[((n+1)//2)-1]}")
else:
    print(f"the median is [{numlist[(n//2)-1]},{numlist[((n+2)//2)-1]}]")



