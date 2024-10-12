#Problem 2
str1 = "programming"
str2 = "prototyping"
AnsStr = ""

for i in range(0,len(str1)):
    if(str1[i] == str2[i]):
        AnsStr = AnsStr + str1[i]
print(AnsStr)