#Problem 4-a
num = int(input("q4 part a input (integer): "))

#With for loop
def starfor(n):
    for i in range(0,n):
        for j in range(0,i):
            print(" ", end="")
    
        for k in range(0,n-i):
            print("*", end="")
        
        print()

starfor(num)

#With while loop
def starwhile(n):
    i = 0
    while(i < n):
        j = 0
        while(j < i):
            print(" ", end="")
            j += 1
    
        k = 0
        while(k < n-i):
            print("*", end="")
            k += 1
    
        print()
        i += 1

starwhile(num)


#Problem 4-b
num = int(input("q4 part b input (integer): "))

#With for loop
l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def alphafor(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(l[j], end="")
        print()

alphafor(num)

#With while loop
def alphawhile(n):
    i = 0
    while(i < n):
        j = 0
        while(j < i+1):
            print(l[j], end="")
            j +=1
    
        print()
        i += 1

alphawhile(num)