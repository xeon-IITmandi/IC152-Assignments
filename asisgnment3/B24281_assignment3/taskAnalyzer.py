#Problem 5-a

def palindrome():

    string = input("Enter a string: ")

    if(string[::-1] == string):
        print("Palindrome")
    else:
        print("Not a Palindrome")

palindrome()

#Problem 5-b

def check():

    N = input("Enter a positive integer: ")

    while(not N.isdigit() or int(N) == 0):
        N = input("Please enter a positive integer: ")

    if(int(N) & 1):
        print("odd")
    else:
        print("even")

check()

#Problem 5-c

def check(string):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVQWXYZabcdefghijklmnopqrstuvwxyz"
    
    for i in string:
        if(not i in alphabet):
            return False
    return True

word = input("Enter a word: ")

if(check(word)):
    print("Alphabet only")
else:
    print("Contains non-alphabetic characters")

#Probelm 5-d

def longest(string):
        l = string.split()
        max = 0
        index = 0

        for i in range(0,len(l)):
            if(len(l[i]) > max):
                  index = i
                  max = len(l[i])
        
        return l[index]

phrase = input("Enter a phrase: ")

print(longest(phrase))

#Problem 5-e

def words(string):
    return len(string.split())

phrase = input("Enter a phrase: ")

print(words(phrase))