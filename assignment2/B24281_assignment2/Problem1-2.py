#Problem 1-2
str1 = input("Enter string_1: ")
str2 = input("Enter string_2: ")
if(str1.find(str2) < 0):
    print("string_2 is not a substring of string_1")
else:
    print("string_2 is a substring of string_1")