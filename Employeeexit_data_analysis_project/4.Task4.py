#Instructions:
#1. Use the Series.value_counts() method to review the unique values in the separationtype column in both 
#   dete_survey_updated and tafe_survey_updated.

#In each of dataframes, select only the data for survey respondents who have a Resignation separation type.
#Remember that the dete_survey_updated dataframe contains three Resignation separation types. We want to select 
#all of them.

#2. Use the DataFrame.copy() method on the result to avoid the SettingWithCopy Warning.
#3. Assign the result for dete_survey_updated to dete_resignations.
#4. Assign the result for tafe_survey_updated to tafe_resignations.

import pandas as pd

dete_survey= pd.read_csv('dete_survey3.csv')
tafe_survey = pd.read_csv('tafe_survey3.csv')

print(dete_survey['separationtype'].value_counts())
print(tafe_survey['separationtype'].value_counts())

#To select all the rows with people that has indicated resignation (all 3 types) in the 
#'seperationtype' column in dete_survey
dete_resignations = dete_survey.loc[(dete_survey['separationtype'] == 'Resignation-Other reasons') | (dete_survey['separationtype'] == 'Resignation-Other employer') | (dete_survey['separationtype'] == 'Resignation-Move overseas/interstate')]
print(dete_resignations)

#To select all the rows with people that has indicated resignation in the 
#'seperationtype' column in tafe_survey
tafe_resignations = tafe_survey.loc[tafe_survey['separationtype'] == 'Resignation']
print(tafe_resignations)

dete_resignations.to_csv('dete_survey4(resignations).csv', index=False)
tafe_resignations.to_csv('tafe_survey4(resignations).csv', index=False)

