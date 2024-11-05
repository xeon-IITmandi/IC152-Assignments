import numpy as np
import matplotlib.pyplot as mpl

np.random.seed(1)
x1=np.linspace(-10,10,1000,endpoint=True)
y1=np.sin(x1)**2
y2=np.cos(x1)**2
y3=y1+y2

mpl.rcParams.update({'font.size': 24}) 

mpl.plot(x1,y1,label="sin\u00B2(x)",color='red')
mpl.title("plot of sin\u00B2(x),cos\u00B2(x) and sin\u00B2(x) + cos\u00B2(x) ")
mpl.xlabel("X-axis")
mpl.ylabel("Y-axis")
mpl.ylim([0.0,1.8])



mpl.plot(x1,y2,label="cos\u00B2(x)",color='blue')
mpl.title("plot of sin\u00B2(x),cos\u00B2(x) and sin\u00B2(x) + cos\u00B2(x) ")
mpl.xlabel("X-axis")
mpl.ylabel("Y-axis")
mpl.ylim([0.0,1.8])



mpl.plot(x1,y3,label="sin\u00B2(x)+cos\u00B2(x)",color='green')
mpl.title("plot of sin\u00B2(x),cos\u00B2(x) and sin\u00B2(x) + cos\u00B2(x) ")
mpl.xlabel("X-axis")
mpl.ylabel("Y-axis")
mpl.ylim([0.0,1.8])


mpl.legend(loc='upper right',fontsize=24,frameon=True,title='Legend')


mpl.show()
