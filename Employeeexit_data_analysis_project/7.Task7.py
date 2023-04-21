#Instructions:
#1. Use the Series.value_counts() method to view the values in the 'Contributing Factors. Dissatisfaction' 
#   and 'Contributing Factors. Job Dissatisfaction' in the tafe_resignations dataframe.
#2. Update the values in the 'Contributing Factors. Dissatisfaction' and 'Contributing Factors. 
#   Job Dissatisfaction' in the tafe_resignations dataframe so that each contains only True, False, 
#   or NaN values.

#Write a function named update_vals that makes the following changes:
#-> If the value is NaN, return np.nan. You can use the following criteria to check that a value 
#   is NaN: pd.isnull(val).
#-> If the value is '-', return False.
#-> For any other value, return True.
#Use the DataFrame.applymap() method to apply the function above to the 'Contributing Factors. 
#Dissatisfaction' and 'Contributing Factors. Job Dissatisfaction' in the tafe_resignations dataframe.

#Remember that we need to pass the update_vals function into the df.applymap() method without parentheses.

#3. Use the df.any() method as described above to create a dissatisfied column in BOTH the 
#   tafe_resignations and dete_resignations dataframes.
import pandas as pd
import numpy as np

dete_survey= pd.read_csv('dete_survey6(resignations).csv')
tafe_survey = pd.read_csv('tafe_survey5(resignations).csv')

def main():
    #1. To check the value counts for some of the columns we deem that the employee is dissatisfied such as the
    #   'job_dissatisfaction' and 'dissatisfaction_with_the_department' columns in the dete_survey dataset.
    #   As we can see, it is already all in Boolean marking (True, False, NaN)
    print(dete_survey['job_dissatisfaction'].value_counts(dropna=False))
    print(dete_survey['dissatisfaction_with_the_department'].value_counts(dropna=False))

    #To check the value counts for the 'Contributing Factors. Dissatisfaction' and 'Contributing Factors. 
    #Job Dissatisfaction' columns in the tafe_survey dataset.
    #As we can see, they are not yet in Boolean hence we need to first change that
    print(tafe_survey['Contributing Factors. Dissatisfaction'].value_counts(dropna=False))
    print(tafe_survey['Contributing Factors. Job Dissatisfaction'].value_counts(dropna=False))

    #2. Making the columns in tafe_survey to only contains True, False or NaN values

    #Note: The usual brute force method
    #tafe_survey.loc[tafe_survey['Contributing Factors. Dissatisfaction'] == 'Contributing Factors. Dissatisfaction ', 'Contributing Factors. Dissatisfaction'] = True
    #tafe_survey.loc[tafe_survey['Contributing Factors. Dissatisfaction'] == '-', 'Contributing Factors. Dissatisfaction'] = False
    #tafe_survey.loc[tafe_survey['Contributing Factors. Job Dissatisfaction'] == 'Job Dissatisfaction', 'Contributing Factors. Job Dissatisfaction'] = True
    #tafe_survey.loc[tafe_survey['Contributing Factors. Job Dissatisfaction'] == '-', 'Contributing Factors. Job Dissatisfaction'] = False
    

    #'apply()', 'map()' and 'applymap()' functions  all works in the same way to applying a function to 
    #each element in a Data Structure. The difference in these functions is to which type of 
    #Data Structure they work for.

    #- 'apply()' works for both DataFrames and Series
    #- 'map()' only works for Series
    #- 'applymap()' only works for DataFrames

    #In this case, we are dealing with a Series so 'applymap()' dosen't work, only 'apply()' and 'map()'
    #works.
    #Using the self made 'update_val' and 'apply()' function
    tafe_survey['Contributing Factors. Dissatisfaction'] = tafe_survey['Contributing Factors. Dissatisfaction'].apply(update_val)
    tafe_survey['Contributing Factors. Job Dissatisfaction'] = tafe_survey['Contributing Factors. Job Dissatisfaction'].apply(update_val)
    print(tafe_survey['Contributing Factors. Dissatisfaction'].value_counts(dropna=False))
    print(tafe_survey['Contributing Factors. Job Dissatisfaction'].value_counts(dropna=False))


    #3. Using the '.any()' function, to create a new column with input True if any of the column (of the same row) 
    #   is True, or False if all the columns (of the same row) is False. (I treated if all NaN or False it will be 
    #   False)
    #(The opposite function of this is '.all()' where if all columns needs to be True for the output to be True
    #and if any 1 is False, the resulting output will be False)
    tafe_survey['dissatisfied'] = tafe_survey[tafe_survey.columns[10:12]].any(axis=1)
    dete_survey['dissatisfied'] = dete_survey.iloc[: , [13,14,15,16,17,18,19,25,26]].any(axis=1)
    print(dete_survey['dissatisfied'].value_counts(dropna=False))
    print(tafe_survey['dissatisfied'].value_counts(dropna=False))

    dete_survey.to_csv('dete_survey7(resignations).csv', index=False)
    tafe_survey.to_csv('tafe_survey6(resignations).csv', index=False)



#Creating the update_val function
def update_val(val):
    if pd.isnull(val):
        return np.nan
    elif val == '-':
        return False
    else:
        return True

main()