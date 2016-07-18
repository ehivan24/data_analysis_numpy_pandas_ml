import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

"""
    T-test checks if the two lists, A & B, are statistically different from each other.

"""


def t_test():
    baseball_data = pd.read_csv('baseball_data.csv')

    #print baseball_data.info()
    print ""

    baseball_player_right = baseball_data[baseball_data['handedness'] == 'R']
    baseball_player_left = baseball_data[baseball_data['handedness'] == 'L']

    result = scipy.stats.ttest_ind(baseball_player_right['avg'], baseball_player_left['avg'], equal_var=False)
    #print result[1]
    if result[1] <= 0.5:
        return False, result
    else:
        return True, result

print t_test()

"""
    Shaphiro-Test utilizes the null hypothesis principle to check
    whether the sample came from normal distributed population.

    - Plot normal distribution.

    if the p-value from the equation shapiro-wilk is less than 0.05,
    this means that, the data did not come from the normal distribution.

    In this case, the p-val is greater than 0.05, 0.05 is the threshold.



"""


def shapiro_test():
    baseball_data = pd.read_csv('baseball_data.csv')

    sorted_baseball_data = sorted(baseball_data['height'])

    w, p = scipy.stats.shapiro(baseball_data['height'])

    print w, p

    if p < 0.05:
        print "Less than 0.05"

    std = np.std(baseball_data['height'])

    mean = np.mean(baseball_data['height'])

    fit = scipy.stats.norm.pdf(sorted_baseball_data, mean, std)

    plt.plot(sorted_baseball_data, fit, '-o')

    plt.hist(sorted_baseball_data, normed=True)

    plt.show()


shapiro_test()

