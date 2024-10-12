#Problem 1-4
string = input("Enter the string: ")
if(string[::-1] == string):
    print("Given string is a palindrome")
else:
    print("Given string is not a palindrome")