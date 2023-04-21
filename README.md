# 9.-Employee-Exit-Data-Analysis-Python :office_worker::arrow_right::door:
A personal project to analyse data from a Employee Exit survey from the Department of Education, Training and Employment (DETE) and the 
Technical and Further Education (TAFE) institute in Queensland, Australia. Python Libraries used: Numpy, Pandas, Matplotlib

## Thoughts on starting this project
My eighth programming project, in Python. 

After my previous programming project on data analysis (8. Star-Wars-Data-Analysis-Python), I wanted to further familiarise myself on the data analysis aspect of
Python programming and its commonly used Python libraries. I spent significantly less time on analysing this dataset and was able to complete more complex tasks such as combining the DETE and TAFE datasets after cleaning them to create a new dataset to use for further data analysis, with more resources to refer on from both the
7.-NumPy-Pandas-Matplotlib-Learning-and-Practice-Python and 8. Star-Wars-Data-Analysis-Python and that I have more tools under my belt for data analysis. (more knowledge of different functions)

<br>

For this Employee Exit Data Analysis Project, we will answer in the guided aspect: **'Are employees who only worked for the institutes for a short period of time resigning due to some kind of dissatisfaction? What about employees who have been there longer?'** and
**Are younger employees resigning due to some kind of dissatisfaction? What about older employees?'**. For the non-guided aspect, we will answer **'How many people in each age group resgined due to some kind of dissatisfaction?'**

<br>

Computer program used for coding: VS Code

## Repository directory description:
Let's start with:
1. Sources and Context
2. Cleaning and Preparing Data
3. Data Modelling and Analysis
4. Analysing Other Aspects of the Dataset

<br>

<br>

**1. Sources and Context**

The Dataquest website provides some guidance and provides the tasks in order to analyse some of the data in the dataset. The 'Employeeexit_data_analysis_project' folder is organised to tasks from the website. '1.Task1.py' to '9.Task9.py' is on Cleaning and Preparing the data while '10.Task10.py' is on Data Modelling and Analysis. '11.Task11.py' is to analyse another aspect of data from the dataset.

I have transferred the tasks from the website as instructions into my respective code files.

Source(s): https://app.dataquest.io/c/60/m/348/guided-project%3A-clean-and-analyze-employee-exit-surveys/1/introduction (Dataquest (main project guide)), 

Datasets analysed [here](https://github.com/plasmagirl/Clean-And-Analyze-Employee-Exit-Surveys/blob/master/dete_survey.csv) (DETE Survey) and [here](https://github.com/plasmagirl/Clean-And-Analyze-Employee-Exit-Surveys/blob/master/tafe_survey.csv) (TAFE Survey)

<br>

<br>

**2.Cleaning and Preparing Data**

_Task 1_
```python
import pandas as pd

dete_survey = pd.read_csv('dete_survey.csv')
tafe_survey = pd.read_csv('tafe_survey.csv')
```
Not much for Task 1, just to load the dataset into the file.(more explanation of the code in comments in the code)

```python
#'.info()' print a concise summary of a DataFrame.
#This method prints information about a DataFrame including the index dtype and columns, 
#non-null values and memory usage.
print(dete_survey.info())
print(dete_survey.head(5))
print(tafe_survey.info())
print(tafe_survey.head(5))
```
To print out the dete_survey and tafe_survey datasets out for checking. Used the '.head(5)' function to only print out the top 5 rows to not flood the output.

'.info()' prints out a concise summary of a DataFrame containing the different names of the column titles, number of non-null values per column, and the data type each column is holding.

<br>

_Task 2_
```python
import pandas as pd

#The 'read_csv()' function actually accepts a lot of different parameters (see documentation), one
#of whuich is 'na_values='
dete_survey = pd.read_csv('dete_survey.csv', na_values='Not Stated')
tafe_survey = pd.read_csv('tafe_survey.csv')

#To check if 'Not Stated' inputs are now NAN
print(dete_survey)
```
For Task 2, the task is to clean the datasets and removing any excess columns that we will not need in this data analysis project. 'na_values='Not Stated'' is to recognise any strings in the dete_survey dataset that has 'Not Stated' as NaN. 

```python
#Dropping columns of index 28 to 49 from the dete_survey dataset
dete_survey_updated = dete_survey.drop(dete_survey.iloc[:, 28:49], axis=1)
print(dete_survey_updated)

#Dropping columns of index 17 to 66 from the dete_survey dataset
tafe_survey_updated = tafe_survey.drop(tafe_survey.iloc[:, 17:66], axis=1)
print(tafe_survey_updated)
```
These lines of code is to remove the indexed columns in the dataset. The indexing for the columns to be removed is provided in the Dataquest guide for this project.

```python
#'index=False' to prevent creating a new column of new indexes in the new csv file
dete_survey_updated.to_csv('dete_survey2.csv', index=False)
tafe_survey_updated.to_csv('tafe_survey2.csv', index=False)
```
Loaded edited dataset into a new file so I can load it into the next code file. And so I can view the dataset as a whole as VS Code dosen't allow me to see the full thing in its terminal. 

As stated in the comment in the code, to prevent from new indexes from keep being added into the dataset, in this task and all the other tasks I included the 'index=False' parameter in the '.to_csv()' function.

<br>

_Task 3_
```python
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

#Removing any spaces at the front and end of the headers
dete_columns_lower_underscore_stripped = []
for element in dete_columns_lower_underscore:
    dete_columns_lower_underscore_stripped.append(element.strip())

```
For task 3, the task is to rename the column titles to something more understandable and standardised.

For the dete_survey dataset:

I made a new list storing all the column titles and working on this new list seperately from the main dataset. I will then later piece the updated column names back into the dataset. 

For renaming of the column titles in the new list, I first changed all the column titles to lowercase (in first for loop), then replacing any spaces into underscore (in second for loop) and lastly removing any spaces at the front and end (in third for loop).

```python
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
```
For adding the new list of renamed column title back into the existing dataset, I had first attached the new list of column titles as the top row of the existing dataset (below the existing/old column titles) from the first chunk of code above (exact description of how each line works is in the code). Then I stored the rest of the dataset minus the top row (the new list of column titles) into a new variable, before declaring the new list of column titles as the headers for the dataset stored in the new variable hence replacing the existing/old column titlesfrom the second chunk of code above(exact description of how each line works is in the code).

```python
#Renaming the column names for the tafe_survey_updated dataset as per requested in Dataquest
tafe_survey_updated = tafe_survey_updated.rename(columns={'Record ID': 'id','CESSATION YEAR': 'cease_date','Reason for ceasing employment': 'separationtype', 'Gender. What is your Gender?': 'gender', 'CurrentAge. Current Age': 'age', 'Employment Type. Employment Type': 'employment_status', 'Classification. Classification': 'position', 'LengthofServiceOverall. Overall Length of Service at Institute (in years)': 'institute_service', 'LengthofServiceCurrent. Length of Service at current workplace (in years)': 'role_service'})

print(tafe_survey_updated.head(5))
```
For tafe_survey dataset:

The Dataquest guide provide the desired column titles for the tafe_survey which I simply used the 'rename()' function that will individually substitute the new titles with the old ones using a dictionary input.

<br>

_Task 4_
```python
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
```
For Task 4, the task is to filter out rows/respondants that indicated they exited the organisation by resignation in both the dete_survey and tafe_survey datasets. 

From '.value_counts()' function we can see there are 3 types of resignation indicated by respondants in the dete_survey ('Resignation-Other reasons', 'Resignation-Other employer' and 'Resignation-Move overseas/interstate'), all of which we will consider as resignation and will filter all 3 of them into consideration.

From '.value_counts()' function we can see there is only 1 type of resignation indicated by respondants in the tafe_survey ('Resignation') which is the only type of respondants we will take into consideration.

<br>

_Task 5_
```python
import pandas as pd

dete_survey= pd.read_csv('dete_survey4(resignations).csv')
tafe_survey = pd.read_csv('tafe_survey4(resignations).csv')

#The 'cease_date' column for dete_survey is currently an object datatype as seen using the 'info()' 
#function and not float so we'll need to convert it so it can more easily used later on in data analysis
print(dete_survey.info())

#The 'cease_date' column for tafe_survey is already a float datatype as seen using the 'info()' 
#function so there is no need for us to convert its data type
print(tafe_survey.info())

#Need to add 'dropna=False' as by default 'dropna=True' which ignores counts of NAN inputs which we do
#not want, as we want to consider them in the counts as well to see the full picture for both dete_survey
#and tafe_survey. 

#We can see there is some issue with dete_survey's 'cease_date' column while tafe_survey's 'cease_date'
#column has no issue. We need to tackle the column for dete_survey
print(dete_survey['cease_date'].value_counts(dropna=False))
print(tafe_survey['cease_date'].value_counts(dropna=False))
```
For task 5, the task is to clean the 'cease_date' column in the dete_survey dataset so that it can be used for later's of calculating the duration of service for respondants in the dete_survey for data analysis. Technically there is no need to check that for the tafe_survey dataset as it already has a duration of service column but we checked its data type anyway.

To check the data type of the 'cease_date' column for both datasets, we used the '.info()' function.

To check the type of values under the 'cease_date' column for both datasets, we used the 'value_counts()' function. 

We discovered that the 'cease_date' column in dete_survey has undesired inputs (strings) that we need to change to floats while the 'cease_date' column in tafe_survey already has the desired data type (float) and no unusual inputs.

```python
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
```
For dete_survey dataset:

To tackle the unusual inputs, it is covered by the comment in the code, using functions such as '.str.split()' and '.str[]' (vectorized string methods)

To tackle the wrong data type, we use the '.astype()' function to convert the data type from object to float.

<br>

_Task 6_
```python
import pandas as pd

#We need an 'institute_service' column in dete_survey so we can compare with its corresponding column
#in the tafe_survey dataset
dete_survey= pd.read_csv('dete_survey5(resignations).csv')

#Subtracting the dete_start_date from the cease_date and assign the result to a new column named 
#institute_service.
dete_survey['institute_service'] = dete_survey['cease_date'] - dete_survey['dete_start_date']

print(dete_survey.head(5))
```
For task 6, the task is to create the 'institute_service' column representing how long the respondant has been with the institute/organisation in the dete_survey dataset as it is missing in this dataset, which we need to compare to the corresponding column in the tafe_survey dataset.

We do this by subtracting the 'dete_start_date' inputs from the 'cease_date' inputs and putting the result in a newly created 'institute_service' column in the dete_survey dataset.

<br>

_Task 7_
```python
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
```
For task 7, the task is to create a 'dissatisfied' column that shows if a respondant has resigned due to dissatisfaction (apart from any other reasons). In the Dataquest guide, we have already identify some factors (as column titles) that we deem as the respondant showing they have exited due to dissatisfaction. Hence, in both datasets, as long as the respondant declared at least one factor (that we deem as a sign of dissatisfaction) a reason for exit, we will show they have resigned due to dissatisfaction and will mark it as True in the 'dissatisfied' column. If none of the factors (that we deem as a sign of dissatisfaction) are a reason for exit, we will show that they did not resign due to dissatisfaction and will mark it as False in the 'dissatisfied' column. If all factors (that we deem as a sign of dissatisfaction) are NaN, we will treat it as False as well.

(Regarding technicalities of the code I will leave it to the comments in the code to explain too much to type otherwise 😫)

```python
#Creating the update_val function
def update_val(val):
    if pd.isnull(val):
        return np.nan
    elif val == '-':
        return False
    else:
        return True

main()
```
This is the function used applied to every single element in the tafe_survey columns 'Contributing Factors. Dissatisfaction' and 'Contributing Factors. Job Dissatisfaction' using the '.apply()' function in the main code. Creating a self-made function and applying the '.apply()' function makes the code look neater compared to the brute force method (that I commented out in the main code)

There is no need to change the elements for the factors (columns) (that we deem as a sign of dissatisfaction) in the dete_survey dataset as they are already in Boolean.

<br>

_Task 8_
```python
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
```
For task 8, the task is to create an 'institute' column in both the dete_survey and tafe_survey dataset and filling its values with 'DETE' and 'TAFE' respectively to indicate which respondant is from which organisation after we combined the 2 datasets. Then, remove any excess columns we do not need for this project's data analysis, ensuring the columns are the same for both datasets and also combining these 2 datasets.

Here, we create the new 'institute' column in both datasets as well as filling said columns.

```python
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
```
Removing excess columns in both datasets we don't need for this project's data analysis and as a good habit, to check to ensure they are removed.

```python
#2. Combining the datasets (top and bottom)
combined_updated = pd.concat([dete_survey_updated, tafe_survey_updated])
print(combined_updated)
print(combined_updated.info())
```
Combining the 2 datasets with the 'pd.concat()' function

```python
#3. Using the 'dropna()' function to drop any rows that has at least 1 NaN value to eliminate any NaN values in our new combined_updated dataset

#The 'inplace=True' parameter is important! By default 'inplace=False' and the 'dropna()' function will return you a
#new modified DataFrame instead of the existing one. In order to modify the existing dataset with 'dropna()'
#you need to make 'inpplace=True'
combined_updated.dropna(axis=0, how='any', inplace=True)
print(combined_updated.info())
```
Now, we try to make the new combined dataset cleaner by removing any rows that contains any NaN values using the '.dropna()' function (take note of the 'inplace=True' parameter!). Data loss is not too bad looking at the '.info()'

<br>

_Task 9_
```python
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
```
For task 9, the task is to create a 'service_cat' column in both the dete_survey and tafe_survey datasets indicating how long a respondant has been working in the organisation. In the Dataquest guide the service categories are defined as 
New: Less than 3 years at a company
Experienced: 3-6 years at a company
Established: 7-10 years at a company
Veteran: 11 or more years at a company

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

<br>

<br>


**3. Data Modelling and Analysis**

Up till now, the cleaning and preparing of the data will enable us to do some data analysis via looking at the patterns of the graphs and answer some questions about the Star Wars survey. In my code, I will see which Star Wars movie was ranked the best? (In Task 5)

I also created a bar graph showing which Star Wars movie has the most views out of the surveyed population. (In Task 6)

I have read in the discussions page in the Dataquest website that using correlation between these 2 graphs, that we may be able to have better insights into data analysis using the '.corr()' function. The code is done by someone else in the discussions page in the Dataquest website which I thought was quite interesting and a way to analyse data that I would want to try in future personal projects.

_Task 5_
```python
import matplotlib.pyplot as plt
import pandas as pd
```
```python
labels = ['Ep 1', 'Ep 2', 'Ep 3', 'Ep 4', 'Ep 5', 'Ep 6']
values = [starwars['rank1'].mean(), starwars['rank2'].mean(), starwars['rank3'].mean(), starwars['rank4'].mean(), starwars['rank5'].mean(), starwars['rank6'].mean()]

plt.bar(labels, values)

plt.title('Bar Graph of Ranking of each Star Wars movie \n (lower ranking, the better the movie)')
plt.xlabel('Star Wars movie')
plt.ylabel('Ranked (lower rank, the better the movie)')

plt.yticks([0,1,2,3,4,5])

plt.savefig('bargraph_rank_each_movie.png', dpi=100)

plt.show()
```

![My Image](bargraph_rank_each_movie.png)

For Task 5, now that we have moved on to modelling data using graphs, I imported the Matplotlib library. The task is to see which was the most highly ranked Star Wars movie. To do this, the dataset asks people to rank the movies in the columns from 1 to 6 (representing Episode 1 to 6), 1 being the best and 6 being the worst. I did this by finding the mean of each column and plotting a bar graph using the mean to find the overall ranking of each Star Wars movie of the surveyed population.

From the graph, we can see that 'Star Wars: Episode V The Empire Strikes Back' has the lowest mean score, which means it was ranked highly by the most people as the best Star Wars movie and 'Star Wars: Episode III Revenge of the Sith' beings the lowest ranked (with the highest mean score).

Learnt how to code for plotting a bar graph in Matplotlib as demonstrated in my previous repository. (7.-NumPy-Pandas-Matplotlib-Learning-and-Practice-Python)

<br>

_Task 6_
```python
labels = ['Ep 1', 'Ep 2', 'Ep 3', 'Ep 4', 'Ep 5', 'Ep 6']
#Using '.sum()' function works because the function treats boolean as values. (1 for True and 0 for False)
#If worried that strings values may affect the result of '.sum()', you can convert all the string values to 0 just in vase
values = [starwars['seen_ep1'].sum(), starwars['seen_ep2'].sum(), starwars['seen_ep3'].sum(), starwars['seen_ep4'].sum(), starwars['seen_ep5'].sum(), starwars['seen_ep6'].sum()]

plt.bar(labels, values)

plt.title('Bar Graph of views of each Star Wars movie')
plt.xlabel('Star Wars movie')
plt.ylabel('Views')

plt.yticks([0,100,200,300,400,500,600,700,800])

plt.savefig('bargraph_views_each_movie.png', dpi=100)

plt.show()

```

![My Image](bargraph_views_each_movie.png)

For Task 6, the task is to see which Star Wars movie has the most views out of the surveyed population. To get the views of each Star Wars movie, since the '.sum()' function treats Boolean markings, True as 1 (and False and NULL as Zero (not relevant but FYI)), by getting the sum of the columns representing each movie, the total sum represents number of people who responded True and have watched each movie.

From the graph, we can see that 'Star Wars: Episode V The Empire Strikes Back' is the most viewed, while 'Star Wars: Episode III Revenge of the Sith' is the least viewed. This is may potentially be due to how well the surveyed population ranked the movie. (Ep 5 highest ranked as the best Star Wars movie, while Ep 3 lowest ranked as the worst Star Wars movie)

<br>

<br>

**4. Analysing Other Aspects of the Dataset**

Task 6 marked the end of the guided part of the data analysis of the Star Wars survey, and that Dataquest recommends that we try to analyse other aspects and find any interesting results from our analysis such as Does, Gender/If the person is a Star Wars fan/If the person is a Star Trek fan, affect the ranking and viewing of each Star Wars movie?

In Task 7 and 7.5, I decided to see whether fans of Star Trek (Task 7) may have a different ranking of the Star Wars movies compared to those that are not fans of Star Trek (Task 7.5).

_Task 7_
```python
a = starwars['Do you consider yourself to be a fan of the Star Trek franchise?']

starwars.loc[a == 'Yes', 'Do you consider yourself to be a fan of the Star Trek franchise?'] = True
starwars.loc[a == 'No', 'Do you consider yourself to be a fan of the Star Trek franchise?'] = False
a.fillna('NaN', inplace=True)

#We can split a DataFrame into two groups based on a binary column by creating two subsets of that column.
watched_st = starwars[a == True]
notwatched_st = starwars[a == False]
```
For Task 7, the task is to get ranking of fans of Star Trek of the Star Wars movies.

This code falls under cleaning and preparing the data section (see Task 2), where I converted 'Yes' responses to the column 'Do you consider yourself to be a fan of the Star Trek franchise?' as True, while 'No' responses to False, and 'NaN' for NULL values for easier manipulation of data during modelling and analysis.

Then I split the 2 groups of people (omitting those that left a NULL value) into 2 variables, 'watched_st' (watched Star Trek) and 'notwatched_st' (Not watched Star Trek)(for Task 7.5).

```python
labels = ['Ep 1', 'Ep 2', 'Ep 3', 'Ep 4', 'Ep 5', 'Ep 6']
values = [watched_st['rank1'].mean(), watched_st['rank2'].mean(), watched_st['rank3'].mean(), watched_st['rank4'].mean(), watched_st['rank5'].mean(), watched_st['rank6'].mean()]

plt.bar(labels, values)

plt.title('Bar Graph of Ranking of each Star Wars movie \n (lower ranking, the better the movie)')
plt.xlabel('Star Wars movie')
plt.ylabel('Points')

plt.yticks([0,1,2,3,4,5])

plt.savefig('bargraph(watchedstartrek)_views_each_movie.png', dpi=100)

plt.show()
```

![My Image](bargraph(watchedstartrek)_rank_each_movie.png)

Getting of the data for fans of Star Trek for the bar graph similar to data modelling and analysis (see Task 5) on taking the mean for the ranking score of each Star Wars movie column.

This graph shows the ranking by fans of Star Trek of the Star Wars movies.

<br>

_Task 7.5_
```python
a = starwars['Do you consider yourself to be a fan of the Star Trek franchise?']

starwars.loc[a == 'Yes', 'Do you consider yourself to be a fan of the Star Trek franchise?'] = True
starwars.loc[a == 'No', 'Do you consider yourself to be a fan of the Star Trek franchise?'] = False
a.fillna('NaN', inplace=True)

#We can split a DataFrame into two groups based on a binary column by creating two subsets of that column.
watched_st = starwars[a == True]
notwatched_st = starwars[a == False]
```
Exact same code as in Task 7, analysing of this code under Task 7.

```python
labels = ['Ep 1', 'Ep 2', 'Ep 3', 'Ep 4', 'Ep 5', 'Ep 6']
values = [notwatched_st['rank1'].mean(), notwatched_st['rank2'].mean(), notwatched_st['rank3'].mean(), notwatched_st['rank4'].mean(), notwatched_st['rank5'].mean(), notwatched_st['rank6'].mean()]

plt.bar(labels, values)

plt.title('Bar Graph of Ranking of each Star Wars movie \n (lower ranking, the better the movie)')
plt.xlabel('Star Wars movie')
plt.ylabel('Points')

plt.yticks([0,1,2,3,4,5])

plt.savefig('bargraph(notwatchedstartrek)_rank_each_movie.png', dpi=100)

plt.show()
```

![My Image](bargraph(notwatchedstartrek)_rank_each_movie.png)

Getting of the data for those who are not fans of Star Trek for the bar graph similar to data modelling and analysis (see Task 5) on taking the mean for the ranking score of each Star Wars movie column.

This graph shows the ranking by those who are not fans of Star Trek of the Star Wars movies.

<br>

_Analysis of Task 7 and Task 7.5 bar graphs_

General ranking of the Star Wars movies by fans and those who are not fans of Star Trek are the same. However, there is a pattern of the difference between the ranking of the top 3 Star Wars movies and the bottom 3 being more significant for those who are fans of Star Trek and those who are not fans of Star Trek (could this be that fans of Star Trek prefer watching the Star Wars movies 4, 5 and 6 more than those who aren't Star Trek fans due to similarities of movies 4, 5, 6 and Star Trek movies?)

<br>

<br>

## Thoughts after the project
This is my first time analysing data using a programming language. I ran into many bugs working with the Star Wars survey dataset such as manipulating of the columns and rows, data type of the values, and how to extract data that I need for analysis. By solving these bugs, I feel that I have learnt a lot and would be able to cleaning, extracting and analysing data much more smoothly with other datasets.

I initially started by previous repository (7.-NumPy-Pandas-Matplotlib-Learning-and-Practice-Python) and learning of NumPy, Pandas and Matplotlib with making a data analysis project as 1 of the goals, glad that I was able to somewhat complete (even though there can still be much improvements) it.

I spent most of my time on figuring out the right commands and fixing bugs at the cleaning and extracting stage and much less time on the drawing the graphs and analysing the data. I believe this is quite normal in the process of analysing data?

<br>

To be improved:
* Some of my codes are quite repetitive, loops/other commands can definitely shorten them.
* Can try to use correlation while analysing the data to find some interesting results.
* Can try working/analysing the data of other columns of the dataset such as 'Education', 'Location (Census Region)', and 'Which character shot first?' to find any interesting patterns to even more completely analyse this Star Wars survey dataset.
* Can try working/analysing the data from columns 15 to 29 (after cleaning the data) as well, which contain data on the characters respondents view favorably and unfavorably to find answers for questions such as 'Which character do respondents like the most?', 'Which character do respondents dislike the most?' and 'Which character is the most controversial (split between likes and dislikes)?'

<br>

Have a gif:

![Semantic description of image](https://media.tenor.com/VdIKn05yIh8AAAAM/cat-sleep.gif)
