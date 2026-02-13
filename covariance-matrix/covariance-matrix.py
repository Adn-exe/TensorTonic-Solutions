import numpy as np

def covariance_matrix(X):
    X = np.asarray(X, dtype = 'float')

    if X.ndim != 2:
        return  None

    n = X.shape[0]
    if n < 2:
        return None 

    feature_mean = np.mean(X, axis = 0)
    X_centered = X - feature_mean
    T_Xcentered = X_centered.T

    sample_cov = (1/(n-1))*np.dot(T_Xcentered, X_centered)
    return sample_cov
    
    