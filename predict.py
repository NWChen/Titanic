#csv reads from and writes to csv files

import csv
import numpy as np

#open the csv file, stream to a Python object
#csv.reader() takes in a csvfile, a delimiter, and a quote character
csv_obj = csv.reader(open('..')) #create object reader
header = csv_obj.next() #skip the first line

data = [] #list to store data
for row in csv_obj:
	data.append(row) #add each line in the .csv to the data list
data = np.array(data) #convert from list to numpy array