import pandas as pd
import numpy as np


titanic_csv = pd.read_csv('titanic_data.csv')
df_titanic = pd.DataFrame(titanic_csv)

#print df_titanic.head()

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


print "Survivors: ",  count_survivors
print "Male count:   ", count_sex_male
print "Female count: ", count_sex_female

print "Total Passengers: ", len(df_titanic['Survived'])

print "Males less than 18 who survived: ", len(predictions_male_under_18)
print "Females less than 18 who survived: ", len(predictions_female_under_18)
print "Males Not under 18 who survived: ", len(not_under_18_males_survived)
print "Females Not under 18 who survived: ", len(not_under_18_females_survived)

print "Not Survived: ", len(not_survived)
print "Age not Registered: ", len(age_not_registered)

print "Total: ", len(not_survived) + len(not_under_18_females_survived) + \
                 len(not_under_18_males_survived) + len(predictions_male_under_18) + \
                 len(predictions_female_under_18) + len(age_not_registered)


passenger_class_1 = {}
passenger_class_2 = {}
passenger_class_3 = {}
for passenger_index_, passenger in df_titanic.iterrows():
    passenger_id = passenger['PassengerId']
    if passenger['Pclass'] == 1:
        passenger_class_1[passenger_id] = 1
    elif passenger['Pclass'] == 2:
        passenger_class_2[passenger_id] = 1
    elif passenger['Pclass'] == 3:
        passenger_class_3[passenger_id] = 1
"""
    Classifies the passenger by class, 1st, 2nd, 3rd.
"""

print "Passengers 1st class: ", len(passenger_class_1)
print "Passengers 2nd class: ", len(passenger_class_2)
print "Passengers 3rd class: ", len(passenger_class_3)

print "Total: ", len(passenger_class_1) + len(passenger_class_2) + len(passenger_class_3)


"""
    Passengers Per class who survived.
"""

passenger_first_class_survivor = {}
passenger_second_class_survivor = {}
passenger_third_class_survivor = {}

passenger_first_class_not_survivor = {}
passenger_second_class_not_survivor = {}
passenger_third_class_not_survivor = {}

for passenger_index__, passenger in df_titanic.iterrows():
    passenger_id = passenger['PassengerId']
    if passenger['Pclass'] == 1 and passenger['Survived'] == 1:
        passenger_first_class_survivor[passenger_id] = 1
    elif passenger['Pclass'] == 2 and passenger['Survived'] == 1:
        passenger_second_class_survivor[passenger_id] = 1
    elif passenger['Pclass'] == 3 and passenger['Survived'] == 1:
        passenger_third_class_survivor[passenger_id] = 1
    elif passenger['Pclass'] == 1 and passenger['Survived'] == 0:
        passenger_first_class_not_survivor[passenger_id] = 1
    elif passenger['Pclass'] == 2 and passenger['Survived'] == 0:
        passenger_second_class_not_survivor[passenger_id] = 1
    elif passenger['Pclass'] == 3 and passenger['Survived'] == 0:
        passenger_third_class_not_survivor[passenger_id] = 1


print "First Class Survivors: ", len(passenger_first_class_survivor)
print "Second Class Survivors:", len(passenger_second_class_survivor)
print "Third Class Survivors:", len(passenger_third_class_survivor)

survived_per_class = len(passenger_first_class_survivor) + \
                         len(passenger_second_class_survivor) + \
                         len(passenger_third_class_survivor)
print "Total Survivors: ", survived_per_class

print "First Class Not Survivors:", len(passenger_first_class_not_survivor)
print "Second Class Not Survivors: ", len(passenger_second_class_not_survivor)
print "Third Class Not Survivors:", len(passenger_third_class_not_survivor)

not_survived_per_class = len(passenger_first_class_not_survivor) + \
                         len(passenger_second_class_not_survivor) + \
                         len(passenger_third_class_not_survivor)

print "Total Not Survivors: ", not_survived_per_class
print "Total: ", not_survived_per_class + survived_per_class

max_price = df_titanic['Fare'].max()
print "Expensive ticket: ", max_price

print df_titanic['Fare'].describe()