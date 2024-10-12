#Problem 3-b
InputStr = input("Enter the string: ")
InputChr = input("Enter the character: ")

InputStr = InputStr.lower()
InputChr = InputChr.lower()

first = -1
last = 0
total = 0

for i in range(0,len(InputStr)):
    if(InputStr[i] == InputChr[0]):
        if(first == -1):
            first = i
        last = i
        total = total + 1
if(first != -1):
    print("first index = " + str(first) +", last index = " + str(last) + ", total occurrences of InputChr =", total)
else:
    print("-1")