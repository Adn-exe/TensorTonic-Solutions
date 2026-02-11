import numpy as np

def mean_squared_error(y_pred, y_true):
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)

    if y_pred.shape !=  y_true.shape:
        return None

    summation = 0
    for i in range(len(y_pred)):
        summation += (y_pred[i] - y_true[i])**2

    mse = (1/len(y_pred))*summation
    return float(mse)