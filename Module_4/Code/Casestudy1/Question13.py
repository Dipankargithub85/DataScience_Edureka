import numpy as np

arr_rand = np.random.rand(3,3)
print (arr_rand)
arr_rand[[0, 2]] = arr_rand[[2, 0]]
print("After Swap")
print(arr_rand)