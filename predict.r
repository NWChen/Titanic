#Windows
#setwd("C:/Users/Neil/Desktop/Research/titanic") #set working directory
#train <- read.csv("C:/Users/Neil/Desktop/Research/titanic/train.csv") #import training set
#test <- read.csv("C:/Users/Neil/Desktop/Research/titanic/test.csv") #import test sample

#Linux
setwd("/home/neil/Desktop/Dev/Titanic")
train <- read.csv("/home/neil/Desktop/Dev/Titanic/train.csv")
test <- read.csv("/home/neil/Desktop/Dev/Titanic/test.csv")

train$Child <- rep(0, length(train$Age)) #populate the Child dimension with 0sA
train$Child[train$Age<=18] <- 1 #rows with Age<=18 are a 1 on the Child dimension

#Survived depends on Child variables and Sex variables
aggregate(Survived ~ Child+Sex, data=train, FUN=sum) #set Survived to Child+Sex subsets, looking at the train dataframe and performing the sum function
aggregate(Survived ~ Child+Sex, data=train, FUN=length) #find total number of people in each subset (child/female, nonchild/female, child/male, nonchild/male)

#calculate aggregated proportions
p <- function(x){
  return(sum(x)/length(x))
  }

aggregate(Survived ~ Child+Sex, data=train, FUN=p)