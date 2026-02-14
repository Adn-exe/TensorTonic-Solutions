import numpy as np

def covariance_matrix(X):
    X = np.asarray(X, dtype = 'float')
    N = X.shape[0]
    
    if X.ndim != 2 :
        return None

    if N < 2:
      return None
    
    X_mean = np.mean(X, axis = 0)
    X_centered = X - X_mean
    T_Xcentered = X_centered.T

    covariance = (1/(N-1))*(np.dot(T_Xcentered, X_centered))
    return covariance