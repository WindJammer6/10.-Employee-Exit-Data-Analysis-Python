#Instructions:
#1. Rename the remaining columns in the dete_survey_updated dataframe. Use the following criteria 
#to update the column names:
#  -> Make all the capitalization lowercase.
#  -> Remove any trailing whitespace from the end of the strings.
#  -> Replace spaces with underscores ('_').
#(e.g. Cease Date should be updated to cease_date.)

#Remember you can use the DataFrame.columns attribute to print an array of the existing column names.

#2. Use the DataFrame.rename() method to update the columns below in tafe_survey_updated. 
#Don't worry about the rest of the column names right now - we'll handle them later.

#3. Use the DataFrame.head() method to look at the current state of the dete_survey_updated and 
#   tafe_survey_updated dataframes and make sure your changes look good.

import pandas as pd

dete_survey_updated = pd.read_csv('dete_survey2.csv')
tafe_survey_updated = pd.read_csv('tafe_survey2.csv')

#Taking out the headers as an array in the dete_survey dataset, and changing all the headers to lowercase
dete_columns = list(dete_survey_updated.columns)
dete_columns_lower = []
for element in dete_columns:
    dete_columns_lower.append(element.lower())

#Changing all the headers' spaces into underscore
dete_columns_lower_underscore = []
for element in dete_columns_lower:
    dete_columns_lower_underscore.append(element.replace(' ', '_')) 

#Removing and spaces at the front and end of the headers
dete_columns_lower_underscore_stripped = []
for element in dete_columns_lower_underscore:
    dete_columns_lower_underscore_stripped.append(element.strip())

#(Copied from online) To add the edited headers array into the dete_survey_updated dataset as top row 
#(below headers)

#Adding a row assigning it with index of -1 and will appear at the bottom of the dataset
dete_survey_updated.loc[-1] = dete_columns_lower_underscore_stripped
#Shifting index causing the newly assigned row to be now of index 0
dete_survey_updated.index = dete_survey_updated.index + 1
#Re-sorting by index so the new row will appear at the top as it is index 0 now
dete_survey_updated = dete_survey_updated.sort_index()

#(Copied from online) To replace headers with top row as the new headers

#Store the first row after the header in a variable
new_header = dete_survey_updated.iloc[0]
#Take all the data less the first row after the header
dete_survey_updated = dete_survey_updated[1:]
#Set the first row as the new dete_survey_updated header
dete_survey_updated.columns = new_header

print(dete_survey_updated.head(5))


#Renaming the column names for the tafe_survey_updated dataset as per requested in Dataquest
tafe_survey_updated = tafe_survey_updated.rename(columns={'Record ID': 'id','CESSATION YEAR': 'cease_date','Reason for ceasing employment': 'separationtype', 'Gender. What is your Gender?': 'gender', 'CurrentAge. Current Age': 'age', 'Employment Type. Employment Type': 'employment_status', 'Classification. Classification': 'position', 'LengthofServiceOverall. Overall Length of Service at Institute (in years)': 'institute_service', 'LengthofServiceCurrent. Length of Service at current workplace (in years)': 'role_service'})

print(tafe_survey_updated.head(5))

dete_survey_updated.to_csv('dete_survey3.csv', index=False)
tafe_survey_updated.to_csv('tafe_survey3.csv', index=False)
