n=int(input("enter the value of n:"))
def factorial(n):
    if n==0 or 1:return 1
    return n*factorial(n-1)
print(factorial(n))