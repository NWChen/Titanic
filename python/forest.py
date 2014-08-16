import pandas as pd
import numpy as np
import csv as csv
from sklearn.ensemble import RandomForestClassifier

#load in training data
train_data = pd.read_csv('C:/Users/Neil/Desktop/Dev/Titanic/train.csv', header=0)

train_data.Gender= train_data.Sex.map({'male':0, 'female':1}).astype(int)
#train_data.
train_data.Embarked = train_data.Embarked.map({'C':0, 'Q':1, 'S':2}).astype(int)

print train_data.head(3)