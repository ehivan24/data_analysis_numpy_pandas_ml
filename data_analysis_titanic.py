import pandas as pd
import numpy as np


titanic_csv = pd.read_csv('titanic_data.csv')
df_titanic = pd.DataFrame(titanic_csv)


count_survivors = count_sex_male = count_sex_female = 0
for survivor in df_titanic['Survived']:
    if survivor == 1:
        count_survivors += 1


for survivor in df_titanic['Sex']:
    if survivor == 'male':
        count_sex_male += 1
    else:
        count_sex_female += 1


predictions_male_under_18 = {}
predictions_female_under_18 = {}
not_under_18_males_survived = {}
not_under_18_females_survived = {}
not_survived = {}
age_not_registered = {}

for passenger_index, passenger in df_titanic.iterrows():
    passenger_id = passenger['PassengerId']
    if (passenger['Sex'] == 'male') and (passenger['Age'] <= 18) and (passenger['Survived'] == 1):
        predictions_male_under_18[passenger_id] = 1
    elif (passenger['Sex'] == 'female') and (passenger['Age'] <= 18) and (passenger['Survived'] == 1):
        predictions_female_under_18[passenger_id] = 1
    elif (passenger['Sex'] == 'male') and (passenger['Age'] > 18) and (passenger['Survived'] == 1):
        not_under_18_males_survived[passenger_id] = 1
    elif (passenger['Sex'] == 'female') and (passenger['Age'] > 18) and (passenger['Survived'] == 1):
        not_under_18_females_survived[passenger_id] = 1
    elif passenger['Survived'] == 0:
        not_survived[passenger_id] = 1
    else:
        age_not_registered[passenger_id] = 1


print "Total Passengers: ", len(df_titanic['Survived'])
print "Survivors: ",  count_survivors

print "Male count:   ", count_sex_male
print "Female count: ", count_sex_female

print "Males less than 18 who survived: ", len(predictions_male_under_18)
print "Females less than 18 who survived: ", len(predictions_female_under_18)
print "Males Not under 18 who survived: ", len(not_under_18_males_survived)
print "Females Not under 18 who survived: ", len(not_under_18_females_survived)

print "Not Survived: ", len(not_survived)
print "Age not Registered: ", len(age_not_registered)

print "Total: ", len(not_survived) + len(not_under_18_females_survived) + \
                 len(not_under_18_males_survived) + len(predictions_male_under_18) + \
                 len(predictions_female_under_18) + len(age_not_registered)
