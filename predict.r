setwd("C:/Users/Neil/Desktop/Research/titanic") #set working directory
train <- read.csv("C:/Users/Neil/Desktop/Research/titanic/train.csv") #import training set
test <- read.csv("C:/Users/Neil/Desktop/Research/titanic/test.csv") #import test sample

train$Child <- rep(0, length(train$Age)) #populate the Child dimension with 0s
train$Child[train$Age<=18] <- 1 #rows with Age<=18 are a 1 on the Child dimension
aggregate(Survived ~ Child+Sex, data=train, FUN=sum) #set Survived to Child+Sex, looking at the train dataframe and performing the sum function