#a
print(6/2/3) #here output is 1 as operations are performed from left to right i.e. 6/2=3 and then 3/3=1
print(6/(2/3))#here output is 9 as first the 2/3 is calculated as it is inside brackets
print((6/2)/3)#here output is 1 as first the 6/2 is calculated as it is inside brackets 


#b
print(2**3**4)#here output is 2**81 as right to left operations are done .
print(2**(3**4))#here also the output is same as first 3**4 is computed as it is inside brackets
print((2**3)**4) #here the output is different which is 8**4 as 2**3 is computed first as it is inside brackets and then the result is raised to 4


# difference observed in first example of part a and b is that the order of operations in part a happens from left to right whereas is part b it happens from right to left

#c
print(2+3<5)#here output is false as 2+3 is 5 
print(2+(3<5))#output is 3 as 2+1 ,here 1 is there because 3<5 is true and the boolean value of true is 1
print((2+3)<5)#here 2+3 is computed and then compared with 5 

# Both the first and third statements evaluate the expression 5 < 5, which is False. Therefore they give the same result

#d
a = 2
b=24 #b can take any value . The result is independent of the value of b.
if (a==2) or (b==3):
	print(True)
	


#e

if (a==2) and (b==3):
	print(True)
	
#now the code will give nameerror as and operator checks the second condition and there it finds b as not defined


