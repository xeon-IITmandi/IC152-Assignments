#function definition
def doubleinput(x):
    print("id(x) in function: ",id(x))
    return x*2

#main program
x=6
print("id(x) in main, 1st:",id(x))

x=doubleinput(x)
print("id(x) in main, 2nd:",id(x))

