#import relevant packages
import csv as csv #math and arrays
import numpy as np #manipulating csv files

'''load in training set'''
#open up the csv file into a Python object
train_file = open('C:/Users/Neil/Desktop/Dev/Titanic/train.csv', 'rb') #separate variable so we can close it later
csv_file_object = csv.reader(train_file) #^read permissions in binary mode
header = csv_file_object.next() #skip the header

data = [] #list
for row in csv_file_object:
	data.append(row) #copy csv to data
data = np.array(data) #convert list to numpy array