#Problem 1-3
string = input("Enter the string: ")
vovels = ["a","e","i","o","u"]
for i in range(0, 5):
    string = string.replace(vovels[i], "?")
print(string)