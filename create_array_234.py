import numpy as np

def create_array_234():
    matrix = np.array([
        [[1,2,3,4], [5,6,7,8], [9,10,11,12]],
        [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
    ])
    return matrix

matrix = create_array_234()
print(matrix.shape)