#Instructions:
#1. Create an institute_service column in dete_resignations
#2. Subtract the dete_start_date from the cease_date. Assign the result to a new column named 
#   institute_service.
import pandas as pd

#We need an 'institute_service' column in dete_survey so we can compare with its corresponding column
#in the tafe_survey dataset
dete_survey= pd.read_csv('dete_survey5(resignations).csv')

#Subtracting the dete_start_date from the cease_date and assign the result to a new column named 
#institute_service.
dete_survey['institute_service'] = dete_survey['cease_date'] - dete_survey['dete_start_date']

print(dete_survey.head(5))

dete_survey.to_csv('dete_survey6(resignations).csv', index=False)



