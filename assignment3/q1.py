#Problem 1-a
import math

n = 15.3245

c = math.ceil(n)
print(c)

f = math.floor(n)
print(f)

r = round(n)
print(r)

print(type(r))
print(format(n))
print(type(format(n)))

print("average:", (f+c+r)/3 )






#Problem 1-b
string = input("Enter a string: ")

print(string.isalpha())
print(string.isnumeric())
print(string.isalnum())
print(string.isspace())