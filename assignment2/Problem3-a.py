#Problem 3-a
InputStr = input("Enter the string: ")
InputChr = input("Enter the character: ")

InputStr = InputStr.lower()
InputChr = InputChr.lower()

first = InputStr.find(InputChr)
last = InputStr.rindex(InputChr)
total = InputStr.count(InputChr)

if(first != -1):
    print("first index = " + str(first) +", last index = " + str(last) + ", total occurrences of InputChr =", total)
else:
    print("-1")