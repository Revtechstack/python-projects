# DATA MANIPULATION & DATA CLEANING
# Context: Clean the CSV file Book.csv, which contains the information about books from the British Library.
# This code performs various data cleaning tasks on the 'Book_dataFile.csv' dataset, 
# including removing unwanted columns, cleaning the 'Date of Publication', 'Author', 'Title', and 'Place of Publication' columns.
# The code uses regular expressions and string manipulation techniques to clean the data and handle missing values appropriately.
# Finally, it displays the cleaned DataFrame for further analysis or use.

import pandas as pd
import re
import numpy as np

def clean_special_char(data_to_clean):
    special_char = r'[,;|...[\\/.\'()\[\]-]'  # no comma here , handle seperately
    # Replace special characters with a space
    cleaned_special_char = re.sub(special_char, '', data_to_clean)
    #print("Hello Special Char", cleaned_special_char)
    return cleaned_special_char

def clean_unwanted_char(data_with_non_ASCII_char):
     
    #convert into string before using encode() - to avoid float value issue by chance
    data_with_non_ASCII_char = str(data_with_non_ASCII_char)
        
    # Remove non-ASCII characters
    data_with_non_ASCII_char = data_with_non_ASCII_char.encode('ascii', 'ignore').decode()
    # Remove leading and trailing whitespace
    data_with_non_ASCII_char = data_with_non_ASCII_char.strip()
    #print(" I am Here ", data_with_non_ASCII_char)
    return data_with_non_ASCII_char

def find_middlename_truncate(first_name):
    #This code removes any characters after the first hyphen ("-") in the first_name string, 
    #if present. Otherwise, it leaves first_name unchanged
    #print("old firstname: ", first_name)
    first_name = first_name[:first_name.find('-')] if '-' in first_name else first_name
    #print("first_name: ", first_name)
    return first_name

## 1 : Read the csv in a data_frame   File:  Book_dataFile.csv
# Read the CSV file into a DataFrame
import pandas as pd 
df = pd.read_csv('Book_manipulation_cleaning.csv')
print(df.info())
#df.info()

##2 : Remove the following columns from the data_frame
'Edition Statement', 
'Corporate Author', 
'Corporate Contributors', 
'Former owner', 
'Engraver', 
'Contributors', 
'Issuance type', 
'Shelfmarks'

# Remove below columns
columns_to_remove = ['Edition Statement', 'Corporate Author', 'Corporate Contributors', 
                     'Former owner', 'Engraver', 'Contributors', 'Issuance type', 'Shelfmarks']
df.drop(columns=columns_to_remove, inplace=True)

#set width
pd.reset_option('display.max_colwidth')
#pd.set_option('display.width', 1500) 
pd.set_option('display.max_columns', 15) 
df.head()

## 3: Check the content of the column- 'Date of Publication’ and define a function to clean the value Examples: 
# For example: 1879 [1878] to: 1879
#              [1858.] to 1858

# DATE OF PUBLICATION

def clean_date_of_publication(date):
    
    date = str(date)
    
    if pd.isna(date) or not date.strip():
        return np.nan  # Return NaN for missing values
    
    # Check if date is not None and not empty string
    if date is not None and date != '':
        # Convert to string if date is not already a string
        if not isinstance(date, str):
            date = str(date)

        # Regular expression to extract the first potential year found in the string
        year_match = re.search(r'\b(\d{4})\b', date)
        
        if year_match:
            # Extracted year
            year_str = year_match.group(1)
            
             # Convert to integer
            year_int = int(year_str)
           
            
            # Check if the year has four digits
            if len(year_str) == 4:
                #print(year_int , type(year_int))
                return (year_int)

    return np.nan  # If no valid year is found or date is None/empty, return NaN


   
  # Clean the Date of Publication column
df['Date of Publication'] = df['Date of Publication'].apply(clean_date_of_publication)   
    
# Fill the null values as 0    
df['Date of Publication'] = df['Date of Publication'].fillna(0)
    
# Convert column to integer type (as this is a float column to avoid populating year in decimal value convert into int column) 
if(~df['Date of Publication'].isna().any()):
    df['Date of Publication'] = df['Date of Publication'].astype(int)

#sort the dataframe by 'Cleaned Date' in descending order
#df.sort_values(by='Cleaned Date', ascending=False)
df[['Date of Publication']][8:15]

# set width
pd.set_option('display.max_columns', 15) 
df.head()

##4: Check the content of the column- ' Author’ and define a function to clean the value. And split the name to first name and last name. 
# AUTHOR
import pandas as pd

# Function to extract first and last names
def extract_first_and_last_names(name):
    
    name = clean_unwanted_char(name)
    
    parts = name.split(',')
    
    if len(parts) == 1:
       
        parts[0] = find_middlename_truncate(parts[0])
        parts[0] = clean_special_char(parts[0])
        series_data = pd.Series({'First Name': parts[0], 'Last Name': ''})
        
        return series_data
    elif len(parts) == 2:
        parts[1] = find_middlename_truncate(parts[1])
        parts[0] = clean_special_char(parts[0])
        parts[1] = clean_special_char(parts[1])
        return pd.Series({'First Name': parts[1], 'Last Name': parts[0]})
    else:
        parts[-1] = find_middlename_truncate(parts[-1])
        parts[-1] = clean_special_char(parts[-1])
        return pd.Series({'First Name': parts[-1], 'Last Name': ''}) 
        #return pd.Series({'First Name': parts[-1], 'Last Name': ', '.join(parts[:-1])})  
    
# Create empty columns 'First Name' and 'Last Name'
df['First Name'] = ''
df['Last Name'] = ''    

# Apply the function to the 'Name' column
df[['First Name', 'Last Name']] = df['Author'].apply(extract_first_and_last_names)

# Display the DataFrame
#pd.set_option('display.max_colwidth', None)  # for max width
  
# mention width to expand
pd.reset_option('display.max_colwidth')
pd.set_option('display.width', 1500) 
pd.set_option('display.max_columns', 5) 
print(df[['First Name', 'Last Name']][230:234]) 

# mention width to expand
pd.reset_option('display.max_colwidth')
pd.set_option('display.width', 1500) 
pd.set_option('display.max_columns', 15) 
df.head()

##5: Check the content of the column- ‘Title’ and define a function to clean the value
#    Examples:
#      ◦ Walter Forbes. [A novel.] By A. A to: Walter Forbes
#       ◦ Love the Avenger. By the author of “All for Gr.. to Love The Avenger 

#TITLE

import re
import pandas as pd

# Define function to clean 'Title'
def clean_title(title):
    title = title.split('By')[0].strip()
    if '.' in title:
        title = title.split('.')[0].strip()
        
    special_char = r'[,;|[\\/.()\[\]-]'
    # Replace special characters with a space
    title = re.sub(special_char, ' ', title)
    
    
    # Remove non-ASCII characters
    title = title.encode('ascii', 'ignore').decode()
    # Remove leading and trailing whitespace
    title = title.strip()
        
    return title

# Clean 'Title' column
df['Title'] = df['Title'].apply(clean_title)

pd.set_option('display.max_colwidth', None)

pd.set_option('display.width', 1000) 
pd.set_option('display.max_columns', 6) 
df[['Title']][5:12] 

pd.set_option('display.width', 1500) 
pd.set_option('display.max_columns', 15) 
print(df.head())

## 6: Check the content of the column- ‘Place of Publication’ and define a function to clean the value.
#  E.g., the original value: London; Virtue & Yorston to: London.
#PLACE OF PUBLICATION


# Function to clean place of publication
def clean_place_of_publication(place):
    
    if place is None or pd.isna(place) or not place.strip():
        return np.nan
    
    # split by ; and remove any unwanted characters
    cleaned_place = place.split(';')[0]  # Split by ";" and take the first part
    cleaned_place = cleaned_place.split(',')[0]  # Split by "," and take the first part
    cleaned_place = cleaned_place.split(':')[0]  # Split by ":" and take the first part
    #cleaned_place = cleaned_place.split(' [')[0]  # Remove anything after "["
    
    cleaned_place1 = clean_unwanted_char(cleaned_place)
    cleaned_place1 = clean_special_char(cleaned_place1)
        
      
    if pd.isna(cleaned_place1) or not cleaned_place1.strip():
        return np.nan   
        
    return cleaned_place1

# Apply cleaning function to the column
df['Place of Publication'] = df['Place of Publication'].apply(clean_place_of_publication)

# Display cleaned data
#df.sort_values(by='Cleaned Date', ascending=False)
print(df[['Place of Publication']][15:20])

print(df.head())
