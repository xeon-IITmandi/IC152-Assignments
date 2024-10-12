#Problem 2

def partA(x):
    if(x >= 10):
        print("High")
    else:
        print("Low")
        
def partB(n):
    if(n > 0):
        print("Positive")
    elif(n < 0):
        print("Negative")
    else:
        print("Zero")

def partC(t):
    if(t == t.upper()):
        print("given string contains only uppercase letters")
    elif(t == t.lower()):
        print("given string contains only lowercase letters")
    else:
        print("given string contains both lowercase and uppercase letters")

def partD(d):
    print(len(d))

def partE(a, b, c):
    print((a+b+c)/3)

x = float(input("\nEnter a floating-point number: "))
partA(x)
    
num = int(input("\nEnter an integer: "))
partB(num)
    
text = input("\nEnter a string: ")
partC(text)

day = input("\nEnter a day of the week: ")
partD(day)

a = float(input("\nEnter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
partE(a,b,c)