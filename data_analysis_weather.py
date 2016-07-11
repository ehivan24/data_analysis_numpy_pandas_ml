import pandas as pd
import numpy as np
import pandasql as pdsql

weather = pd.read_csv('weather_underground.csv')

#print weather.info()
#print weather.head()


def number_of_raining_day(df_weather):
    weather_data = pd.read_csv(df_weather)

    q = """
        SELECT * FROM weather_data WHERE maxpressurem > 1010
    """
    rainy_days = pdsql.sqldf(q.lower(), locals())
    return rainy_days


print number_of_raining_day('weather_underground.csv')
