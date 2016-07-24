import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ggplot import *
import seaborn as sns
sns.set()


weather = pd.read_csv('weather_underground.csv')
df_weather = pd.DataFrame(weather)
print df_weather.keys()
#plt.figure()
#plt.plot(df_weather['heatingdegreedaysnormal'], df_weather['since1julheatingdegreedaysnormal'])
#plt.show()

print ggplot(df_weather, aes('since1julheatingdegreedaysnormal', 'heatingdegreedaysnormal')) \
      + geom_point(color='blue') \
      + geom_line(color='red') \
      + ggtitle('since1julheatingdegreedaysnormal') \
      + xlab('Year') + ylab('heatingdegreedaysnormal')

