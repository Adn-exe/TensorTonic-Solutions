import numpy as np

def covariance_matrix(X):
  X = np.asarray(X, dtype = 'float')
  N = X.shape[0]

  if N < 2 or X.ndim != 2:
    return None

  sample_mean = np.mean(X, axis = 0)
  X_centered = X - sample_mean
  Transpose_Xcentered = X_centered.T

  mat_mul = np.dot(Transpose_Xcentered, X_centered)
  Cov_matrix = (1/(N-1))*mat_mul

  return Cov_matrix