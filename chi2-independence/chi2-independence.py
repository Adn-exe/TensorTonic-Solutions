import numpy as np

def chi2_independence(C):
    c = np.asarray(C, dtype= 'float')

    row_sum = c.sum(axis = 1)
    col_sum = c.sum(axis = 0)
    
    exp_frequency = np.outer(row_sum, col_sum)/c.sum()
    chi_sqr = np.sum((c - exp_frequency)**2 / exp_frequency)
    return chi_sqr, exp_frequency