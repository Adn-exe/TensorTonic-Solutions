import numpy as np

def matrix_transpose(A):
    A = np.array(A)
    m, n = A.shape

    arr = np.zeros((n, m))
    for i in range(m):
        for j in range(n):
            arr[j, i] = A[i, j]
    return arr