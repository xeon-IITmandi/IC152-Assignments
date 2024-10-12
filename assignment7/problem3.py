#function definition
def f(p,b=5):
    return (p**2+b**2)**(0.5)

p=float(input("enter the value of perpendicular p:"))
b=float(input("enter the value of base b:"))

print("h=",f(p,b))