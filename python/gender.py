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

'''sample displaying'''
#print '1: ' + np.array_str(data[0])
#print '-1: ' + np.array_str(data[-1])
#print '0, 3: ' + np.array_str(data[0,3])

'''calculate the proportion of survivors'''
number_passengers = np.size(data[0::,1]) #size of column 1 (0-indexed), Survived, from row 0 to end
number_survived = np.sum(data[0::,1].astype(np.float)) #sum of the elements in column 1 (1 or 0 -> #people survived)
proportion_survivors = number_survived/number_passengers

'''isolate rows in which Sex is female'''
women_only_stats = data[0::,4] == "female"
men_only_stats = data[0::,4] != "female"

'''specifically the Survived column'''
women_onboard = data[women_only_stats,1].astype(np.float)
men_onboard = data[men_only_stats,1].astype(np.float)

'''find proportion of survivors by gender'''
proportion_women_survived = np.sum(women_onboard)/np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard)/np.size(men_onboard)

print 'Proportion of women who survived is %s' % proportion_women_survived
print 'Proportion of men who survived is %s' % proportion_men_survived

'''read test data'''
test_file = open('C:/Users/Neil/Desktop/Dev/Titanic/test.csv', 'rb')
test_file_object = csv.reader(test_file)
header = test_file_object.next()

'''write gender model as a csv'''
prediction_file = open('C:/Users/Neil/Desktop/Dev/Titanic/python/gendermodel.csv', 'wb') 
prediction_file_object = csv.writer(prediction_file)
prediction_file_object.writerow(["PassengerId", "Survived"]) #header
for row in test_file_object: #each row in test.csv
	if row[3] == "female": #Sex is female
		prediction_file_object.writerow([row[0], '1'])
	else:
		prediction_file_object.writerow([row[0], '0'])

train_file.close()
test_file.close()
prediction_file.close()

