import pandas as pd
import numpy as np
import csv as csv
from sklearn.ensemble import RandomForestClassifier

#load in data
train_data = pd.read_csv('C:/Users/Neil/Desktop/Dev/Titanic/training.csv', header=0)
test_data = pd.read_csv('C:/Users/Neil/Desktop/Dev/Titanic/test.csv', header=0)

#convert objects to numbers
train_data.Gender = train_data.Sex.map({'male':0, 'female':1}).astype(int)
train_data.Embarked[train_data.Embarked.isnull()] = train_data.Embarked.dropna().mode().values #fill	
train_data.Embarked = train_data.Embarked.map({'C':0, 'Q':1, 'S':2}).astype(np.int64)

#ages with no data -> make median
median_age = train_data.Age.dropna().median()
train_data.loc[(train_data.Age.isnull()), 'Age'] = median_age

#fill in missing Fares
median_fare = np.zeros(3);
for f in range(0, 3):
	median_fare[f] = test_data[test_data.Pclass==f+1]['Fare'].dropna().median()
for f in range(0, 3):
	test_data.loc[(test_data.Fare.isnull())&(test_data.Pclass==f+1), 'Fare'] = median_fare[f]


#drop unnecessary columns
train_data = train_data.drop(['Name', 'Sex', 'Ticket', 'Cabin', 'PassengerId'], axis=1)

#clean up test data set too
test_data.Gender = test_data.Sex.map({'male':0, 'female':1}).astype(int)
test_data.Embarked[test_data.Embarked.isnull()] = test_data.Embarked.dropna().mode().values
test_data.Embarked = test_data.Embarked.map({'C':0, 'Q':1, 'S':2}).astype(np.int64)
median_age = test_data.Age.dropna().median()
test_data.loc[(test_data.Age.isnull()), 'Age'] = median_age
median_fare = np.zeros(3)
for f in range(0, 3):
	median_fare[f] = test_data[test_data.Pclass==f+1]['Fare'].dropna().median()
for f in range(0, 3):
	test_data.loc[(test_data.Fare.isnull())&(test_data.Pclass==f+1), 'Fare'] = median_fare[f]

#removal of unnecessary test columns
ids = test_data.PassengerId.values
test_data = test_data.drop(['Name', 'Sex', 'Ticket', 'Cabin', 'PassengerId'], axis=1)

#do I really need this?
train_data = train_data.values
test_data = test_data.values

#create random forest object
forest = RandomForestClassifier(n_estimators = 100)

#fit training data to Survived labels
forest = forest.fit(train_data[0::,1::], train_data[0::,0])

#run decision trees on test data
output = forest.predict(test_data)

print(output)

predictions_file = open('C:/Users/Neil/Desktop/Dev/Titanic/python/predictions.csv', 'wb')
open_file_object = csv.writer(predictions_file)
open_file_object.writerow(["PassengerId", "Survived"])
open_file_object.writerows(zip(ids, output))
predictions_file.close()

print("COMPLETE");

