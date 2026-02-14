import numpy as np

def matrix_inverse(A):
  A = np.array(A, dtype = 'float')
  I = np.eye(A.shape[0])
  
  if A.ndim != 2 and A.shape[0] != A.shape[1]:
    return None
    
  if np.linalg.det(A) == 0:
    return None

  A_inv = np.linalg.inv(A)
  error = np.linalg.norm(np.dot(A, A_inv) - I)

  if error < 1e-7:
    return A_inv
  else:
    return None
    
  
    