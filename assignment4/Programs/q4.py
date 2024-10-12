#Problem 4-a
print("\nq4 part a\n")

def maxOfThree(numList):
    l = []
    for i in range(1,len(numList)-1):
        l.append(max(numList[i-1],numList[i],numList[i+1]))
    return l

numList =  [1,4,2,9,11,10,19,5,12]

print("function input:", numList)
print(maxOfThree(numList))

#Problem 4-b
print("\n\nq4 part b\n")

m = int(input("q4 part b input (no. of rows): "))
n = int(input("q4 part b input (no. of columns): "))

matrix  = []

for i in range(0,m):
    matrix.append(eval(input("Enter row " + str(i) + ": "))[:n])

for i in matrix:
    for j in i:
        print(j,end=" ")
    print()

#Problem 4-c
print("\n\nq4 part c\n")

num2DList = []
output=[]

n = 3
m = 3

for i in range(0,len(numList[:m*n]),m):
    num2DList.append(numList[i:m+i])

for i in num2DList:
    output.append(maxOfThree(i))

print("n = ", n, "and m = ", m)
print(output)

print("\n\n")