file1=open(r'C:\Users\prate\OneDrive\Documents\B24281_assignment2\inputWithErrors.txt','r')
file2=open(r'C:\Users\prate\OneDrive\Documents\B24281_assignment2\outputClean.txt','w')
a=file1.readlines()
file2.write(a[0].title())
a.pop(0)
for i in a:
    b=i.capitalize()  
    c=b.replace(' .','.')
    d=c.replace(' ,',',')
    e=d.replace(' )',')')
    f=e
    if '(' in e and e[e.find('(')-1:e.find('(')]!=' (':
        f=e.replace('(',' (')
    file2.write(f)
file1.close()
file2.close()
