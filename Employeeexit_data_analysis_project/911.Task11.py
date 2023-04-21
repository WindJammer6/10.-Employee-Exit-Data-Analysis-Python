#Instructions:
#1. Clean the age column. 
#2. How many people in each age group resgined due to some kind of dissatisfaction?
import pandas as pd
import matplotlib.pyplot as plt

combined_updated = pd.read_csv('combined_updated.csv')

def main():
    #Checking all the different types of values present in the 'age' column. (Noticed there are no NaN values as we
    #cleared them earlier in the project already)
    print(combined_updated['age'].value_counts(dropna=False))

    #I plan to split the age groups into 6 groups:
    #-> <21
    #-> 21 to 30
    #-> 31 to 40 
    #-> 41 to 50 
    #-> 51 to 60 
    #-> >60

    #Cleaning the age column (I plan to split the current values into a list and taking only the first element)
    #First split those values with spaces and taking the first element
    combined_updated['age'] = combined_updated['age'].str.split(' ').str[0]
    print(combined_updated['age'].value_counts(dropna=False))

    combined_updated['age'] = combined_updated['age'].str.split('-').str[0]
    print(combined_updated['age'].value_counts(dropna=False))

    #Making the data type of the 'age' column into floats
    combined_updated['age'] = combined_updated['age'].astype(float)

    #Creating a function and mapping it to the 'age' column to split the respondants to different age groups and 
    #assigning the age groups to an 'age_group' column
    combined_updated['age_group'] = combined_updated['age'].apply(age_group)
    print(combined_updated['age_group'].value_counts(dropna=False))
    print(combined_updated.head(5))

    #Plotting out the results in a bar graph
    #5. Plotting the results in a bar graph
    xaxis = ['21 to 30', '31 to 40', '41 to 50', '51 to 60', '<21', '>60']

    #Creating a pivot table and using the new 'dissatisfied' column given to us in the pivot table as the 
    #y-axis data
    dissatisfied_pivot_table = pd.pivot_table(combined_updated, index='age_group', values='dissatisfied', aggfunc='count')
    print(dissatisfied_pivot_table)
    yaxis = dissatisfied_pivot_table['dissatisfied']

    plt.bar(xaxis, yaxis)

    plt.title('Bar Graph of Number of Resigned Dissatisfied Employees\n(by Age Group)')
    plt.xlabel('Age Group')
    plt.ylabel('Number of Resigned Dissatisfied Employees')

    plt.yticks([0,20,40,60,80,100,120,140,160,180])

    plt.savefig('bargraph(number_of_dissatisfied_employees_(by_age_group)).png', dpi=100)

    plt.show()


#Creating the age_group function
def age_group(val):
    if val < 21:
        return '<21'
    elif val >= 21 and val <= 30:
        return '21 to 30'
    elif val >= 31 and val <= 40:
        return '31 to 40'
    elif val >= 41 and val <= 50:
        return '41 to 50'
    elif val >= 51 and val <= 60:
        return '51 to 60'
    elif val > 60:
        return '>60'

main()