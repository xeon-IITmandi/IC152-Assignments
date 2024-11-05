import numpy as np
import matplotlib.pyplot as mpl

# random_integers=np.random.randint(2e5,size=100)

random_integers=np.linspace(-10e5,10e5,100)
mean=np.mean(random_integers)
median=np.median(random_integers)

# random_integers[98]=mean
# random_integers[99]=median

# x_values=random_integers.copy()

y1=[]
for i in range(len(random_integers)):
    y1.append(np.sum(random_integers[i]-random_integers) **2)

y2=[]
for i in range(len(random_integers)):
    y2.append(np.abs(random_integers[i]-random_integers))

mpl.subplot(1,2,1)
mpl.plot(random_integers,y1,label='mean',color='red')
mpl.title("Plot1-mean")
mpl.xlabel("X-axis")
mpl.ylabel("Y-axis")


mpl.subplot(1,2,2)
mpl.plot(random_integers,y2,label='median',color='blue')
mpl.title("Plot2-median")
mpl.xlabel("X-axis")
mpl.ylabel("Y-axis")



mpl.show()

