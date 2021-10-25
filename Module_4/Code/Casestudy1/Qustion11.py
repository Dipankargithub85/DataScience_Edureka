import numpy as np

arr_rand = np.random.rand(3,3)
print(arr_rand[arr_rand[:, 1].argsort()])