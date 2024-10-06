import math
def sincosval(a):
    def cos(x):
        return math.sin(a-x)
    return cos

print(sincosval(math.pi/2)(math.pi))







