#qa
n=int(input("enter value of n:"))
def f(n):
    if n==0 :return 1
    elif n==1:return 3
    return f(n-1)+f(n-2)

print(f(n))


#qb
list1=[1,3]
j=int(input("enter value of n in f(n):"))
for i in range(j):
    list1.append(list1[len(list1)-2]+list1[len(list1)-1])
print(list1[j])


#c
# The recursive implementation is less efficient due to the overhead of the call stack, which can lead to higher memory usage for larger n.
#The non-recursive implementation uses memory efficiently by only maintaining a list of computed values, resulting in a more stable and predictable memory footprint.




