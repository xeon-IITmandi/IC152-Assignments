#a
# creating tuples
W = 1920
H = 1080
C = 3
WHC_tuple1 = (W, H, C)
print(WHC_tuple1)
WHC_tuple2 = W, H, C # brackets in tuple are optional, commas are not
print(WHC_tuple2)

for element in WHC_tuple1:
    		print(element)

PI = 3.14 #this is a simple floating point number, not a tuple
print(PI)

PI_tuple = 3.14, #note there is a comma in the end
print(PI_tuple)

Origin_tuple = 0, 0
print(Origin_tuple)


#b
# indexing is possible in tuples
a = (1,2,3,4,5,6)
print(a[2])
print(a[4:])


#c
# code1:
# tuple = ('hi', 2, 4.32, True)
# a[2] = 7

# # code 2
# tuple = ('A','B', 'C')
# tuple.append('D')


#d
#trick to change the elements of a tuple
#we will change the elements of tuple a
a=list(a)
a[2]=5
#now 3rd element of tuple will be changed from 3  to 5
a=tuple(a)
print(a)#prints (1, 2, 5, 4, 5, 6)