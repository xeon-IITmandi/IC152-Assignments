#Problem 3-a
print("\nq3 part a\n")

def place(l,n):
    return l[len(l)-n-1]

coeffs = eval(input("q3 part a input (list):"))
n = int(input("q3 part a input (integer):"))

print(place(coeffs,n))

#Problem 3-b
print("\n\nq3 part b\n")

x = int(input("q3 part b input (integer):"))

print(4*x**3 - 6*x**2 - 1)

#Problem 3-c
print("\n\nq3 part c\n")

sup = "⁰¹²³⁴⁵⁶⁷⁸⁹"

f1 = eval(input("q3 part c input (list):"))
f2 = eval(input("q3 part c input (list):"))
f3 = []

if(len(f1) < len(f2)):
    for i in range(0,len(f2)-len(f1)):
        f1.insert(0,0)
elif(len(f2) < len(f1)):
    for i in range(0,len(f1)-len(f2)):
        f2.insert(0,0)

for i in range(0,len(f1)):
    f3.append(f1[i] + f2[i])

deg = len(f3)-1
notFirst = False
for i in range(0,deg-1):
    if(not f3[i] == 0):
        if(notFirst):
            if(f3[i] == abs(f3[i])):
                print(" + " + str(f3[i]) + "x" + sup[deg-i], end="")
            else:
                print(" - " + str(abs(f3[i])) + "x" + sup[deg-i], end="")
        else:
            print(str(f3[i]) + "x" + sup[deg-i], end="")
            notFirst = True

if(notFirst):
    if((not f3[deg-1] == 0) & (not deg == 0)):
        if(f3[deg-1] == abs(f3[deg-1])):
            print(" + " + str(f3[deg-1]) + "x", end="")
        else:
            print(" - " + str(abs(f3[deg-1])) + "x", end="")
else:
    if((not f3[deg-1] == 0) & (not deg == 0)):
        print(str(f3[deg-1]) + "x", end="")
        notFirst = True

if(notFirst):
    if(not f3[deg] == 0):
        if(f3[deg] == abs(f3[deg])):
            print(" + " + str(f3[deg]), end="")
        else:
            print(" - " + str(abs(f3[deg])), end="")
else:
    if(not f3[deg] == 0):
        print(str(f3[deg]), end="")

print("\n\n")