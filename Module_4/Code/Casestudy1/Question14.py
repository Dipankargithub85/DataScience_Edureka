import numpy as np
random_matrix_array = np.random.rand(3, 4)
print(random_matrix_array)
print ('Matrix rank:',np.linalg.matrix_rank(random_matrix_array))
