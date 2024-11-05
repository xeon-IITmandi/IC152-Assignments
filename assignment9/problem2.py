import numpy as np

np.random.seed(1)
random_floats=np.random.normal(size=20)
print(random_floats)

np.random.seed()
random_floats_2=np.random.normal(size=20)
print(random_floats_2)