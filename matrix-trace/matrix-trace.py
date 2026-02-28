import numpy as np

def matrix_trace(A):
  A = np.array(A)

  if A.ndim != 2 and A.shape[0] != A.shape[1]:
    raise ValueError

  mat_trace = 0
  for i in range(len(A[0])):
    mat_trace += A[i][i]

  return mat_trace
  
