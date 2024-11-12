#a
# setA = {20, 30, 10}
# setB = {20, 30, 40}
# print(setA & setB) #intersection 
# print(setA - setB)#difference of sets
# print(setA | setB)#union
# for element in setA:
#     print(element)

#b
# setA = {20, 30, 10}
# print(setA[1:])#uncomment this to see error
#we get a typeerror'TypeError: 'set' object is not subscriptable ' this is because sets don't have indexing so they can't be sliced 

#c
setA = {20, 30, 10}
setA.add(40)
print(setA)
setA.remove(20)
print(setA)
popped_element = setA.pop()
print(popped_element, setA)
print(setA.issubset({10,30,50}))
setA.union({10, 20})
print(setA)

setC = set() # if you use {} instead of set() you will get an error think why after doing q 4
for i in range(10):
	setC.add(i//2)
print(setC)

#d
l=[1,2,3,2,4,2,1]
print(set(l))

def my_set(input_list):
	temp_set=[]
	for el in input_list:
		if el not in temp_set:
			temp_set.append(el)
	print(temp_set)
    

my_set(l)