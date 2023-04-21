#Instructions:
#1. Read the dete_survey.csv CSV file into pandas again, but this time read the Not Stated values 
#   in as NaN. To read Not Stated in as NaN, set the na_values parameter to Not Stated in the 
#   pd.read_csv() function. Assign the result to dete_survey.
#2. Then, let's drop some columns from each dataframe that we won't use in our analysis to make the 
#   dataframes easier to work with. Use the DataFrame.drop() method to drop the following columns from 
#   dete_survey: dete_survey.columns[28:49]. Remember to set the axis parameter equal to 1. 
#   Assign the result to dete_survey_updated.
#3. Use the DataFrame.drop() method to drop the following columns from tafe_survey: tafe_survey.columns[17:66]. 
#   Remember to set the axis parameter equal to 1. Assign the result to tafe_survey_updated.

import pandas as pd

#The 'read_csv()' function actually accepts a lot of different parameters (see documentation), one
#of whuich is 'na_values='
dete_survey = pd.read_csv('dete_survey.csv', na_values='Not Stated')
tafe_survey = pd.read_csv('tafe_survey.csv')

#To check if 'Not Stated' inputs are now NAN
print(dete_survey)

#Dropping columns of index 28 to 49 from the dete_survey dataset
dete_survey_updated = dete_survey.drop(dete_survey.iloc[:, 28:49], axis=1)
print(dete_survey_updated)

#Dropping columns of index 17 to 66 from the dete_survey dataset
tafe_survey_updated = tafe_survey.drop(tafe_survey.iloc[:, 17:66], axis=1)
print(tafe_survey_updated)

#'index=False' to prevent creating a new column of new indexes in the new csv file
dete_survey_updated.to_csv('dete_survey2.csv', index=False)
tafe_survey_updated.to_csv('tafe_survey2.csv', index=False)
