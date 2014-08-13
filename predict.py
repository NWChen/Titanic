#csv reads from and writes to csv files

import csv
import numpy as np

#open the csv file, stream to a Python object
#csv.reader() takes in a csvfile, a delimiter, and a quote character
csv_obj = csv.reader(open("training.csv","rb")) #create object reader; open file with read permissions in binary mode
header = csv_obj.next() #skip the first line

data = [] #list to store data
for row in csv_obj:
	data.append(row) #add each line in the .csv to the data list
data = np.array(data) #convert from list to numpy array

passengers = np.size(data[0::,1].astype(np.float)) #convert csv strings to floats for calculations
survivors = np.sum(data[0::,1].astype(np.float)) 
proportion_of_survivors = survivors/passengers;

women_only_stats = data[0::,4] == "female" #find all elements in the gender column with value female
men_only_stats = data[0::,4] != "female" #find all elements in the gender column with non-female value (male)

women_onboard = data[women_only_stats,1].astype(np.float) #in column 1 (Survived), all the rows for which column 4 (gender) registers True for female
men_onboard = data[men_only_stats,1].astype(np.float)

proportion_women_survived = np.sum(women_onboard)/np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard)/np.size(men_onboard)

print(proportion_men_survived)
print(proportion_women_survived)