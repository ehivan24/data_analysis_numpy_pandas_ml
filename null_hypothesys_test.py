import numpy
import matplotlib.pyplot as plt
from collections import Counter
import scipy.stats

town1_heights = [5, 6, 7, 6, 7.1, 6, 4]
town2_heights = [5.5, 6.5, 7, 6, 7.1, 6]

town1_mean = numpy.mean(town1_heights)
town2_mean = numpy.mean(town2_heights)

print "Mean town 1: ", town1_mean

print "Mean town 2: ", town2_mean

print "Effective Size: ", abs(town1_mean - town2_mean)

increment = 1
width = .25

town1_bucketted = map(lambda ammt: ammt - ammt%increment, town1_heights)
town2_bucketted = map(lambda ammt: ammt - ammt%increment + width, town1_heights)
town1_hist = Counter(town1_bucketted)
town2_hist = Counter(town2_bucketted)

minamount = max(min(town1_heights), min(town2_heights))
maxammount = max(max(town1_heights), max(town2_heights))

print "Min: ", minamount
print "Max: ", maxammount

print "Town_1 Shapiro-Wilks p-value: ", scipy.stats.shapiro(town1_heights)[1]
print "Town_2 Shapiro-Wilks p-value: ", scipy.stats.shapiro(town2_heights)[1]

print "Mann-Whitney p-value: ", scipy.stats.mannwhitneyu(town1_heights, town2_heights)[1]


fig = plt.figure()
sub = fig.add_subplot(111)
sub.bar(town1_hist.keys(), town1_hist.values(), color='b', width=width, label='town 1')
sub.bar(town2_hist.keys(), town2_hist.values(), color='r', width=width, label='town 2')

sub.legend()

plt.show()

