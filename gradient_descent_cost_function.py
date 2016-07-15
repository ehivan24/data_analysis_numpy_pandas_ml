import pandas
import numpy


def compute_cost(features, values, theta):
    """
    compute the cost of a list of values.

    J(theta) = (1 / 2m) * sum(h(x^i) - Y^2)^2

    :param features: list of features
    :param values: input values
    :param theta: output data points
    :return: cost of a list of parameters
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features - theta) - values).sum()
    cost = sum_of_square_errors / (2 * m)
    return cost

