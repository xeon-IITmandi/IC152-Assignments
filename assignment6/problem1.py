def sumab(a):
    
    def sumb(b):
       
        return a + b
    return sumb

f = sumab(20)

print(f(10))

'''
algorithm of the above code:

a function sumab is made to store some value in variable a . It has a nested function sumb which takes argument and stores it in variable b. The fucntion sumab when called doesnt compute a result immediately but returns another function which can be called later. The function sumb computes the value of the sum of a and b . The function sumab is called with a=20 and the value it returns is assigned to variable f. So in a way f is now sumb. Now f is called with argument 10 which means sumb is called with b=10. The function sumb calculated sum of a and b that is 20 and 10 which equals 30. Now this result is printed using print function. '''
   
'''The scope of variable a in the function sumb() is local.'''



