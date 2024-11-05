#function definition
def squareinputlist(x):
    print("id(x) in function: ",id(x))
    return [el**2 for el in x]


#main program
x_list=eval(input("enter integers to be added in the list: "))
print("id(x) in main, 1st: ",id(x_list))

x_list=squareinputlist(x_list)

print("id(x) in main, 2nd: ",id(x_list))



