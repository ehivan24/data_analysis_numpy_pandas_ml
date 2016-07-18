import numpy as np
from scipy import stats


def compute_r_square(data, predictions):

    """
    R^2 = 1 - sum(y_i - f_i)^2 / sum(y_i - y(hat))^2

    :param data: y_i ... y_n
    :param predictions: f_i ... f_n

    :return: R^2
    """
    data = np.array(data)
    predictions = np.array(predictions)
    mean = np.mean(data)

    r_squared = 1 - np.square(data - predictions).sum() / np.square(data - mean).sum()
    return r_squared


data = [1, 2, 3, 4, 5]
predictions = [1, 3, 2, 4, 5]

print "R^2: ", compute_r_square(data, predictions)
gradient, intercept, r_value, p_value, std_err = stats.linregress(data, predictions)

print gradient, intercept, r_value, p_value, std_err

