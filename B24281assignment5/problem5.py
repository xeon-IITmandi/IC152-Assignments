N=int(input("enter the no. of sublists:"))
parentlist=[]
def sublistmaker(k):
    childlist=[]
    for i in range(y):
        x=float(input(f"enter element no.{i+1} in sublist no.{k+1}:"))
        childlist.append(x)
    parentlist.append(childlist)



for j in range(N):
    y=int(input(f"enter no. of elements in sublist no.{j+1}:"))
    sublistmaker(j)

# print(parentlist)

avglist=[]
for sublist in parentlist:
    sum=0
    for j in sublist:
        sum+=j
        mean=sum/len(sublist)
    avglist.append(mean)    



print(avglist)






