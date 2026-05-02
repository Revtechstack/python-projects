# This python file load CSV file, read data from CSV file and manipulation using that data

#Import proper library for loading csv file, and open the csv file
# Import pandas
import pandas as pd


# Load the CSV File "StudentsInformation.csv"
df_Students_Information = pd.read_csv("C:/Workspace/StudentsInformation.csv")
print("hello")

#Read the records from the csv file and print each student’s First name, Middle name and Last name.
# Get the student 'First name','Second name','Last name'
df_display_StudInfo = df_Students_Information[['First name','Second name','Last name']]

#change column name to upper - for better look  
df_display_StudInfo.columns = df_display_StudInfo.columns.str.upper() 


#Print each student’s student 'First name','Second name','Last name'
print("\n\n")
print(df_display_StudInfo.to_string(index=False))         #Remove the index while display values - for clear understanding
print("\n\n")

## Calculate the mean age of the students.
#Import numpy
import numpy as np

# Calculate the mean age of the students
age = df_Students_Information['Age']
print("\n\n Students Mean-Age:  ", np.mean(age), "\n\n")
