import numpy as np

arr = np.array([np.nan,1,2,np.nan,3,4])

print(arr)

output1 = arr[np.logical_not(np.isnan(arr))]
print(output1)