import numpy as np
array = np.arange(10)
newarr3 = array[np.logical_and(array != 3, array != 9)]
print(newarr3)


