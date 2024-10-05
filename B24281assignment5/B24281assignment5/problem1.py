numlist=[]
for i in range(10):
    x=float(input(f"enter no. {i+1}:"))
    numlist.append(x)
sum=0
for num in numlist:
    sum+=num
print(sum/len(numlist))    

