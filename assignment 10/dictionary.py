#a

studentDict = {"name": "Raghav", "age": 18, "marks": 97.25}
print(studentDict ["name"])
print(studentDict ["marks"])

for key in studentDict:
	print(key)

for key in studentDict:
	print(studentDict[key])

for key in studentDict.keys():
	print(key)

for value in studentDict.values():
	print(value)

for item in studentDict.items():
	print(item)

#b
mySquareDict = {}
for i in range(5):
	mySquareDict[i] = i**2
print(mySquareDict)

popped_Value = mySquareDict.pop(4)
print(popped_Value, mySquareDict)

#c
# myCubeDict = {3: 27, 4: 64}
# print(myCubeDict[0]) #uncomment lines 30 & 31
#we are trying to access the value of the key 0 but the key 0 doesn't exist therefore it raises a keyError

#d
l=[1,2,3,2,4,2,1]
temp_set=set(l)

dict={el: l.count(el) for el in temp_set}
print(dict)


#e

l=[10,14,100]

temp_set=set(l)
temp_list=list(temp_set)
factors=[]
for i in range(len(temp_list)):
    temp=[]
    for j in range(1,temp_list[i]+1):
        if temp_list[i]%j==0:
            temp.append(j)
    factors.append(temp)
	


dict={temp_list[i]:factors[i] for i in range(len(temp_list))}

print(dict)