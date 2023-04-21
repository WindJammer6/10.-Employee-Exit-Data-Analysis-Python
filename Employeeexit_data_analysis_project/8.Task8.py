#Instructions:
#1. First, let's add a column to each dataframe that will allow us to easily distinguish between the two.
#   -> Add a column named institute to dete_resignations_up. Each row should contain the value DETE.
#   -> Add a column named institute to tafe_resignations_up. Each row should contain the value TAFE.
#2. Combine the dataframes.
#Recall that we still have some columns left in the dataframe that we don't need to complete our analysis. 
#3. Use the DataFrame.dropna() method to drop any columns with less than 500 non null values.
#Remember that you can drop columns with less than a certain number of non null values with the thresh parameter.
#Assign the result to combined_updated.
import pandas as pd

dete_survey= pd.read_csv('dete_survey7(resignations).csv')
tafe_survey = pd.read_csv('tafe_survey6(resignations).csv')

#1. Adding a new 'institute' column to both datasets with all its values as 'DETE' and 'TAFE' respectively
dete_survey['institute'] = 'DETE'
tafe_survey['institute'] = 'TAFE'

#To check the columns are added
print(dete_survey.head(5))
print(tafe_survey.head(5))

print(dete_survey.info())
print(tafe_survey.info())

#Removing excess columns that we won't need in our data analysis. 
#From both the dete_survey and tafe_survey datasets we will only keep the columns 'id', 'seperationtype', 'gender', 'age', 
#'institute_service', 'dissatisfied' and 'institute' (from earlier in this code)
dete_survey_updated = dete_survey[['id', 'separationtype', 'gender', 'age', 'institute_service', 'dissatisfied', 'institute']]
tafe_survey_updated = tafe_survey[['id', 'separationtype', 'gender', 'age', 'institute_service', 'dissatisfied', 'institute']]

#To check the excess columns are removed
print(dete_survey_updated.head(5))
print(tafe_survey_updated.head(5))

print(dete_survey_updated.info())
print(tafe_survey_updated.info())

#2. Combining the datasets (top and bottom)
combined_updated = pd.concat([dete_survey_updated, tafe_survey_updated])
print(combined_updated)
print(combined_updated.info())

#3. Using the 'dropna()' function to drop any rows that has at least 1 NaN value to eliminate any NaN values in our
#   new combined_updated dataset

#The 'inplace=True' parameter is important! By default 'inplace=False' and the 'dropna()' function will return you a
#new modified DataFrame instead of the existing one. In order to modify the existing dataset with 'dropna()'
#you need to make 'inpplace=True'
combined_updated.dropna(axis=0, how='any', inplace=True)
print(combined_updated.info())

combined_updated.to_csv('combined_updated.csv', index=False)
