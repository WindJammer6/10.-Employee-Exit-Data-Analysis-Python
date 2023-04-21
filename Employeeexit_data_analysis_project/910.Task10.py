#Instructions
#1. Use the Series.value_counts() method to confirm if the number of True and False in the dissatisfied column. 
#   -> Set the dropna parameter to False to also confirm the number of missing values.
#2. Use the DataFrame.fillna() method to replace the missing values in the dissatisfied column with the value that 
#   occurs most frequently in this column, either True or False.
#3. Use the DataFrame.pivot_table() method to calculate the percentage of dissatisfied employees in each service_cat 
#   group.
#4. Since a True value is considered to be 1, calculating the mean will also calculate the percentage of dissatisfied
#   employees. The default aggregation function is the mean, so you can exclude the aggfunc argument.
#5. Use the DataFrame.plot() method to plot the results. Set the kind parameter equal to bar to create a bar chart.
#   Make sure to run %matplotlib inline beforehand to show your plots in the notebook.
import pandas as pd
import matplotlib.pyplot as plt

combined_updated = pd.read_csv('combined_updated2.csv')

#1 and 2. As we can see from this code, we only have True or False values in the 'dissatisfied' column as we have already
#   decided to drop all the rows with NaN values in any of the columns. We may have lost some data, but it is not
#   a significant lost during this cleaning process
print(combined_updated['dissatisfied'].value_counts(dropna=False))

#3 and 4. Using the '.pivot_table()' function to create a pivot table. It takes many parameters (see documentation). 
#   -> The first parameter is the name of dataframe
#   -> 'index=' represents the row headers
#   -> 'values=' represents the column headers
#   -> 'aggfunc=' (by default will be mean so technically no need put here but I just did it so its clear), 
#      represents what operator to use (see documentation for list of accepted operators). Since the values are all =
#      Boolean and Python can take Boolean values as int 1 (for True) and 0 (for False), finding mean will give
#      us percentage of respondants that said True and False for dissatisfied, and categorized by their service_cat
#      shown in row header in the pivot table
dissatisfied_pivot_table = pd.pivot_table(combined_updated, index='service_cat', values='dissatisfied', aggfunc='mean')
print(dissatisfied_pivot_table)

#5. Plotting the results in a bar graph
xaxis = ['Established', 'Experienced', 'New', 'Veteran']
#Using the new 'dissatisfied' column given to us in the pivot table as the y-axis data
yaxis = dissatisfied_pivot_table['dissatisfied']

plt.bar(xaxis, yaxis)

plt.title('Bar Graph of Percentage of Resigned Dissatisfied Employees\n(by Service Category)')
plt.xlabel('Service Category')
plt.ylabel('Percentage of Resigned Dissatisfied Employees\n(vs other reasons for exiting the company)')

plt.yticks([0,0.1,0.2,0.3,0.4,0.5,0.6])

plt.savefig('bargraph(resigned_dissatisfied_employees_(by_service_category)).png', dpi=100)

plt.show()

