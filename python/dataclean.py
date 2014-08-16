#import relevant packages
import csv as csv #math and arrays
import numpy as np #manipulating csv files
import pandas as pd
import pylab as P

'''load in training set'''
#build a Pandas dataframe
df = pd.read_csv('C:/Users/Neil/Desktop/Dev/Titanic/train.csv', header=0)

#map Sex (male, female) to M, F or 0, 1
df['Gender'] = df['Sex'].map(lambda x: x[0].upper())
df['Gender'] = df['Sex'].map({'female':0, 'male':1}).astype(int)

#map Embarked
#df['Onboard'] = df['Embarked'].map({'C':0, 'Q':1, 'S':2}).astype(int)

#2x3 median age reference table; 2 Genders, 3 Pclasses
median_ages = np.zeros((2,3))

#populate the array
for i in range(0, 2):
	for j in range(0, 3):
		median_ages[i, j] = df[(df['Gender']==i)&(df['Pclass']==j+1)]['Age'].dropna().median()

#make a copy of Age (columns)
df['AgeFill'] = df['Age']

#all rows in which Age is null and specified columns
#note column indexing can be dataframe['label'] or just dataframe.label
#print(df[df.Age.isnull()][['Gender','Pclass','Age','AgeFill']].head(10))

for i in range(0, 2):
	for j in range(0, 3):
		df.loc[(df.Age.isnull())&(df.Gender==i)&(df.Pclass==j+1), 'AgeFill'] = median_ages[i, j]
df[df.Age.isnull()][['Gender','Pclass','Age','AgeFill']].head(10)
df['AgeIsNull'] = pd.isnull(df.Age).astype(int)


'''feature engineering'''
#parch: number of parents/children onboard
#sibsp: number of siblings or spouses

'''clean and fill'''


df['FamilySize'] = df['SibSp'] + df['Parch']
df['Age*Class'] = df.AgeFill * df.Pclass #amplify older ages
print(df.dtypes[df.dtypes.map(lambda x:x=='object')])