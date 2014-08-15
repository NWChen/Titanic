#FOR THE GRAPHICS - BE SURE TO INSTALL (install.packages()):
#rattle
#rpart.plot
#RColoBrewer
#(then run library())

#Windows
#setwd("C:/Users/Neil/Desktop/Research/titanic") #set working directory
#train <- read.csv("C:/Users/Neil/Desktop/Research/titanic/train.csv") #import training set
#test <- read.csv("C:/Users/Neil/Desktop/Research/titanic/test.csv") #import test sample

#Linux
setwd("/home/neil/Desktop/Dev/Titanic")
results <- read.csv("/home/neil/Desktop/Dev/Titanic/r/results.csv")
train <- read.csv("/home/neil/Desktop/Dev/Titanic/train.csv")
test <- read.csv("/home/neil/Desktop/Dev/Titanic/test.csv")

#import
library(rpart)

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

#bin fares into $10 categories
train$FareType <- rep('30+', length(train$Fare))
train$FareType[train$Fare<10] <- '<10'
train$FareType[train$Fare>=10 & train$Fare<20] <- '10<20'
train$FareType[train$Fare>=20 & train$Fare<30] <- '20<30'

#aggregate with new fare categories
aggregate(Survived ~ FareType + Pclass + Sex, data=train, FUN=p)

#having noticed that women in 3rd class with a $20+ ticket fared poorly in terms of survival, build a new prediction
test$Survived <- 0
test$Survived[test$Sex=='female'] <- 1
test$Survived[test$Sex=='female' & test$Pclass==3 & test$Fare>=20] <- 0

#build decision tree on survival, passenger class, sex, age, #siblings/spouses aboard, #parents/children aboard, fare, port of embarkation
#survival is categorical, so run class instead of anova
#class function for factor (categorical variable)
fit <- rpart(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked, data=train, method="class")

#prettify decision tree
plot(fit)
text(fit)