#Instructions:
#Check the years in each dataframe for logical inconsistencies.

#1. Clean the cease_date column in dete_resignations.
#  ->Use the Series.value_counts() method to view the unique values in the cease_date column.
#  ->Use vectorized string methods to extract the year.
#  ->Use the Series.astype() method method to convert the type to a float.
#  ->Use the Series.value_counts() to check the values in the cease_date and dete_start_date 
#    columns in dete_resignations and the cease_date column in tafe_resignations.
#  ->Because Series.value_counts() returns a series, we can use Series.sort_index() method with 
#    ascending= True or False to view the highest and lowest values with their counts.

#You can also plot the values of any numeric columns with a boxplot to identify any values that look wrong.

import pandas as pd

dete_survey= pd.read_csv('dete_survey4(resignations).csv')
tafe_survey = pd.read_csv('tafe_survey4(resignations).csv')

#The 'cease_date' column for dete_survey is currently an object datatype as seen using the 'info()' 
#function and not float so we'll need to convert it so it can more easily used later on in data analysis
print(dete_survey.info())

#The 'cease_date' column for tafe_survey is already a float datatype as seen using the 'info()' 
#function so there is no need for us to convert its data type
print(tafe_survey.info())

#Need to add 'dropna=False' as by default 'drop=na=True' which ignores counts of NAN inputs which we do
#not want, as we want to consider them in the counts as well to see the full picture for both dete_survey
#and tafe_survey. 

#We can see there is some issue with dete_survey's 'cease_date' column while tafe_survey's 'cease_date'
#column has no issue. We need to tackle the column for dete_survey
print(dete_survey['cease_date'].value_counts(dropna=False))
print(tafe_survey['cease_date'].value_counts(dropna=False))


#(Copied from online) It can split the string using the slash as the delimiter into 2 elements 
#in a list and only selecting the last element (from the '.str[-1]' function from the list as the input 
#(which will always be the year be it the list has one or two elements as the year will always be the 
#first element from the back (last element))
dete_survey['cease_date'] = dete_survey['cease_date'].str.split('/').str[-1]

#By checking here we can see that we removed the inputs with months and gave us a more accurate number of 
#the counts of how many people resigned from the dete_survey per year
print(dete_survey['cease_date'].value_counts(dropna=False))

#Converting data type of the 'cease_date' column for the dete_survery from object to a float
dete_survey['cease_date'] = dete_survey['cease_date'].astype(float)

#To check if the data type for the 'cease_date' column for the dete_survery has indeed changed 
print(dete_survey.info())


#To print out final dete_survey's and tafe_survey's value counts
print(dete_survey['cease_date'].value_counts(dropna=False).sort_index(ascending=True))
print(tafe_survey['cease_date'].value_counts(dropna=False).sort_index(ascending=True))


dete_survey.to_csv('dete_survey5(resignations).csv', index=False)
tafe_survey.to_csv('tafe_survey5(resignations).csv', index=False)








