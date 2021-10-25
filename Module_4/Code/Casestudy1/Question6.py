import numpy as np
li= [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
arr=np.array(li)
arr_filtered = arr[np.where(arr > 5 )]
print(arr_filtered)