import pandas as pd
import numpy as np
import scipy.stats

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
    print result[1]
    if result[1] <= 0.5:
        return False, result
    else:
        return True, result

print t_test()




