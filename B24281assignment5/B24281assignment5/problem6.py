import math
def summision(vals):
    sum=0
    for i in vals:
        sum+=i
    return sum

def prodSummision(m,n):
    sum=0
    for i in range (0,len(m),1):
        sum+=(m[i])*(n[i])
    return sum

def summision_squares(vals):
    sum=0
    for i in vals:
        sum+=i**2
    return sum

def find_mean(z):
    return (sum(z)/len(z))

def vector(mean,list):
    listNew=[]
    for i in range(0,len(list),1):
        d=list[i]-mean
        listNew.append(d)
    return listNew


a=int(input('Enter number of entries for list:'))
list_x=[]
for i in range(0,a):
    val=int(input(f'Enter num{i+1} for list_x:'))
    list_x.append(val)

list_y=[]
for i in range(0,a):
    val=int(input(f'Enter num{i+1} for list_y:'))
    list_y.append(val)
print(list_x)
print('sum of x:',summision(list_x))
print(list_y)
print('sum of y:',summision(list_y))
#print(prodSummision(list_x,list_y))
r = (a*prodSummision(list_x, list_y)-(summision(list_x)*summision(list_y)))/(math.sqrt((a*summision_squares(list_x)-(summision(list_x))**2)*(a*summision_squares(list_y)-(summision(list_y))**2)))

print('Correlation=',r)
e=find_mean(list_x)
f=find_mean(list_y)
X=vector(e,list_x)
Y=vector(f,list_y)
ratio=prodSummision(X,Y)/((math.sqrt(summision_squares(X)))*(math.sqrt(summision_squares(Y))))
print('Ratio:',prodSummision(X,Y)/((math.sqrt(summision_squares(X)))*(math.sqrt(summision_squares(Y)))))


if round(r,5)==round(ratio,5):
    print('Correlation=Ratio')
else:
    print('Not true')