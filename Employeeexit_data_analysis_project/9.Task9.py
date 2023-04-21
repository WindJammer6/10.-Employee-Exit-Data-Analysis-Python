#Instructions:
#Cleaning the 'institute_service' column.

#1. First, we'll extract the years of service from each value in the institute_service column.
#   -> Use the Series.astype() method to change the type to 'str'.
#   -> Use vectorized string methods to extract the years of service from each pattern. You can find the full list of 
#      vectorized string methods here.
#   -> Double check that you didn't miss extracting any digits.
#   -> Use the Series.astype() method to change the type to 'float'.
#
#2. Create a function that maps each year value to one of the career stages above. Then, we'll map each value 
#   to one of the career stage definitions. (New: Less than 3 years at a company, Experienced: 3-6 years at a 
#   company, Established: 7-10 years at a company, Veteran: 11 or more years at a company)
#   -> Remember that you'll have to handle missing values separately. You can use the following code to check if a 
#      value is NaN where val is the name of the value: pd.isnull(val).
#   -> Use the Series.apply() method to apply the function to the institute_service column. 
#   -> Assign the result to a new column named service_cat.
import pandas as pd

combined_updated = pd.read_csv('combined_updated.csv')

def main():

    #1. To view the types of values present in the 'institute_service' column
    print(combined_updated['institute_service'].value_counts())
    print(combined_updated.info())

    #There are string values 'Less than 1 year' and 'More than 20 years' in the 'institute_service' column that 
    #we need to deal with. I decided to convert the 'Less than 1 year' values to just a value of 1 and 'More than 
    #20 years' value to a value of 20
    combined_updated.loc[combined_updated['institute_service'] == 'Less than 1 year', 'institute_service'] = 1
    combined_updated.loc[combined_updated['institute_service'] == 'More than 20 years', 'institute_service'] = 20

    #Checking the values in the 'institute_service' column again
    print(combined_updated['institute_service'].value_counts())

    #There are string values '1-2', '3-4', '5-6' '7-10' and '11-20' in the 'institute_service' column that we also
    #need to deal with. I decided to use vectorized string method to split them into a list with '-' as the
    #delimiter and taking the first element in those lists as the new value
    combined_updated['institute_service'] = combined_updated['institute_service'].str.split('-').str[0]

    #Checking the values in the 'institute_service' column again
    print(combined_updated['institute_service'].value_counts())

    #Using the Series.astype() method to change the type of the 'institute_service' column to 'float'
    combined_updated['institute_service'] = combined_updated['institute_service'].astype(float)

    #Checking the values in the 'institute_service' column again as well as its data type
    print(combined_updated['institute_service'].value_counts())
    print(combined_updated.info())

    #Applying the 'career_stage' function to the 'institute_service' column and adding the new labels into a new
    #column 'service_cat'
    combined_updated['service_cat'] = combined_updated['institute_service'].apply(career_stage)
    print(combined_updated['service_cat'].value_counts())
    print(combined_updated.info())

    combined_updated.to_csv('combined_updated2.csv', index=False)

#Creating the career_stage function
def career_stage(val):
    if val < 3:
        return 'New'
    elif val >= 3 and val <= 6:
        return 'Experienced'
    elif val > 6 and val <= 10:
        return 'Established'
    elif val > 10:
        return 'Veteran'


main()