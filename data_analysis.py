### EFFECTIVE DATA ANALYSIS BY APPLYING DESCRIPTIVE STATISTICS

###### Context:
    
""" The Boston Housing Dataset is a derived from information collected by the U.S. Census Service concerning housing in the area of Boston MA. The following describes the dataset columns:

    • CRIM - per capita crime rate by town
    • ZN - proportion of residential land zoned for lots over 25,000 sq.ft.
    • INDUS - proportion of non-retail business acres per town.
    • CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)
    • NOX - nitric oxides concentration (parts per 10 million)
    • RM - average number of rooms per dwelling
    • AGE - proportion of owner-occupied units built prior to 1940
    • DIS - weighted distances to five Boston employment centres
    • RAD - index of accessibility to radial highways
    • TAX - full-value property-tax rate per $10,000
• PTRATIO - pupil-teacher ratio by town
• B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
• LSTAT - % lower status of the population
• MEDV - Median value of owner-occupied homes in $1000's    """

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
### QUESTION 1: Load Dataset from Boston Housing Agency into a DataFrame.
# Load Dataset from Boston Housing Agency.csv
df = pd.read_csv("boston_housing_data_analysis.csv")
df.head()

### 2: For the "Median value of owner-occupied homes" provide a boxplot. 
# BOXPLOT - "Median value of owner-occupied homes" 

plt.figure(figsize=(6, 4))
# Adjust outlier appearance
sns.boxplot(x='MEDV', data=df, color='lightgreen', linewidth=2, flierprops=dict(marker='o', markersize=6
                                                                                , markerfacecolor='red', linestyle=''
                                                                                , label='Out Layer')) 
plt.title('Boxplot: Median Value of Owner-Occupied Homes\n', fontsize =14)
plt.xlabel('Median Value ($1000)', fontsize =12)

# Add median line
plt.axvline(df['MEDV'].median(), color='red', linestyle='--', label='Median Value')  
plt.legend(fontsize=10)
plt.show()

# 2 continue - REMOVING THE OUTLIERS
# "Median value of owner-occupied homes" 

# Interquartile Range (IQR) method to identify outliers in the 'MEDV' column of in df.

# Calculate quartiles and IQR
Q1 = df['MEDV'].quantile(0.25)
Q3 = df['MEDV'].quantile(0.75)
IQR = Q3 - Q1

# Define lower and upper bounds for outliers 
# A common approach in statistics for identifying outliers based on the data
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter outliers
# Any value below Q1 - 1.5 * IQR or above Q3 + 1.5 * IQR is considered an outlier
df_no_outliers = df[(df['MEDV'] >= lower_bound) & (df['MEDV'] <= upper_bound)]

# Display statistics
print("Before removing outliers:\n")
print("Number of data points:", len(df))
print("Minimum MEDV:", df['MEDV'].min())
print("Maximum MEDV:", df['MEDV'].max())

print("\nAfter removing outliers:\n")
print("Number of data points:", len(df_no_outliers))
print("Minimum MEDV:", df_no_outliers['MEDV'].min())
print("Maximum MEDV:", df_no_outliers['MEDV'].max())

# 2 continue: BOXPLOT WITHOUT OUTLIERS

plt.figure(figsize=(6, 4))
sns.boxplot(x='MEDV', data=df_no_outliers, color='lightgreen', linewidth=2)

plt.title('Without outliers : Median Value of Owner-Occupied Homes (in $1000)\n', fontsize =14)
plt.xlabel('Median Value ($1000)')
# Add median line
plt.axvline(df_no_outliers['MEDV'].median(), color='red', linestyle='--', label='Median Value')  
plt.legend(fontsize=10)
plt.show()

###3: Provide a histogram for the “Charles river variable”. 
# histogram for the “Charles river variable

plt.figure(figsize=(6, 4))
sns.histplot(df['CHAS'], bins=2, color ='brown') 
plt.title('\nHistogram of Charles River Variable (CHAS)\n')
plt.xlabel('Charles River Variable')

# Add gridlines
plt.grid(True)  
plt.show()

### 4: Provide a boxplot for the MEDV variable vs the AGE variable. (Discretize the age variable into three groups of 35% or less, between 35 and 70% and 70% and over) 
# Discretize the AGE variable into three groups

# AGE does not have negative value so no need of -np.inf

df['AGE_group'] = pd.cut(df['AGE'], bins=[0, 35, 70, np.inf], labels=['35% or less', 'between 35 and 70%', '70% and over'])
df.head()

# BOXPLOT for MEDV vs AGE

plt.figure(figsize=(6, 4))
sns.boxplot(x='AGE_group', y='MEDV', data=df)
plt.title('\nBoxplot of Median value of owner-occupied homes (MEDV) vs AGE group\n', fontsize =14)
plt.xlabel('AGE group',fontsize =12)
plt.ylabel('MEDV')
plt.show()

### 5: Provide a scatter plot to show the relationship between Nitric oxide concentrations (NOX) and the proportion of non-retail business acres per town (INDUS). What can you say about the relationship?
# Provide a scatter plot for NOX vs INDUS

import matplotlib.pyplot as plt
import seaborn as sns

# Set style for seaborn
sns.set_style("whitegrid")

#set the context for a larger font scale
sns.set_context("talk")

# Create the scatter plot with customized attributes
plt.figure(figsize=(6, 4))

 # s=45 --> size of the scatterplot circle    
sns.scatterplot(x='NOX', y='INDUS', data=df, color='green', s =45)

# Add titles and labels
plt.title('\nRelationship between Nitric oxide concentrations (NOX) VS Non-retail business (INDUS)\n', fontsize=16)
plt.xlabel('NOX (parts per 10 million)', fontsize=12)
plt.ylabel('INDUS (proportion)', fontsize=12)

# Add grid lines for better readability
plt.grid(True, linestyle='--', alpha=0.4)

# Show plot
plt.show()

# 5 continue : RELATIONSHIP - say about the relationship between Nitric oxide concentrations (NOX) and the proportion of non-retail business acres per town (INDUS)

# Pearson correlation coefficient --> it's a common measure used to quantify the linear relationship between two continuous variables


from scipy.stats import pearsonr

# Calculate the Pearson correlation coefficient
correlation_coefficient, p_value_pearson = pearsonr(df['NOX'], df['INDUS'])

print(f"\nPearson Correlation Coefficient: {correlation_coefficient}\n")
print(f"P-value_pearson: {p_value_pearson}\n")

sig_level_alpha = 0.05 

if p_value_pearson < sig_level_alpha:
    # Reject the Null Hypothesis
    print("The correlation is statistically significant - a strong positive correlation between nitric oxide concentration and the proportion of non-retail business")
else:
    #Fail to reject the Null Hypothesis
    print("The correlation is not statistically significant - there is not enough evidence to support the presence of a significant relationship between nitric oxide concentration and the proportion of non-retail business.")

### QUESTION 6: Create a histogram for the pupil to teacher ratio variable (PTRATIO)
# Create a histogram for the pupil to teacher ratio variable (PTRATIO)

import matplotlib.pyplot as plt
import seaborn as sns

# Set style and context for seaborn
sns.set_style("whitegrid")
sns.set_context("paper")

# Create the histogram with customized attributes
plt.figure(figsize=(6, 4))
sns.histplot(df['PTRATIO'], bins=20, color='blue', edgecolor='black')

# Add titles and labels
plt.title('\nHistogram: Pupil to Teacher ratio variable (PTRATIO)\n', fontsize=16)
plt.xlabel('PTRATIO', fontsize=14)
plt.ylabel('Frequency', fontsize=14)


# Add vertical grid lines for better readability
# alpha parameter to control the transparency 
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.show()

### QUESTION 7: Is there a significant difference in median value of houses bounded by the Charles river or not? (CHAS) (T-test for independent samples)
# T-test for median values of houses bounded by Charles river (CHAS)

#Rejecting the null hypothesis means --> we have found evidence to suggest that there is a statistically
#significant difference between the means of the two groups being compared

# calculate significant difference in median value of houses between houses bounded by the Charles River 
#and those are not bounded by the river


from scipy.stats import ttest_ind

# Subset the data based on charless river value(0 or 1)
river_houses = df[df['CHAS'] == 1]['MEDV']
nonriver_houses = df[df['CHAS'] == 0]['MEDV']

# Perform t-test  ## p-->probability 
t_stat, p_value = ttest_ind(river_houses, nonriver_houses)


# Define significance level - consider as alpha
sig_level_alpha = 0.05 


# Interpret the p-value  - #sig_level_alpha --> significant level, # .2f -->2 decimal places floating point number
if p_value < sig_level_alpha:
    #Rejecting the null hypothesis
    print(f'\nTest Statistic: {t_stat:.2f}\n')
    print(f'P-value: {p_value}\n')
    print('There is a significant difference in median house values between houses bounded by the Charles River \nand not bounded by the river.\n')
else:
    #Fail to reject the null hypothesis 
    print(f'Test Statistic: {t_stat:.2f}')
    print(f'P-value: {p_value:.2f}')
    print('There is not enough evidence to conclude a significant difference in median house values.')

    ### QUESTION 8: Is there a difference in Median values of houses (MEDV) for each proportion of owner occupied units built prior to 1940 (AGE)? (ANOVA)
    # ANOVA for median values of houses based on AGE groups - already age_group created in df for previous qn 

from scipy.stats import f_oneway

age_groups = [df[df['AGE_group'] == group]['MEDV'] for group in df['AGE_group'].unique()]


#assessing whether there are statistically significant differences in the means of multiple groups.
f_stat, p_value_anova = f_oneway(*age_groups)
print(f'\nANOVA p-value for MEDV across different AGE groups: {p_value}\n')


# Define significance level - consider as alpha
sig_level_alpha = 0.05 


# Interpret the p_value_anova  - #sig_level_alpha --> significant level, # .2f -->2 decimal places floating point number
if p_value_anova < sig_level_alpha:
    #Rejecting the null hypothesis
    print(f'\nTest Statistic: {f_stat:.2f}\n')
    print(f'P-value_anova: {p_value_anova}\n')
    print('There is a significant difference in median house values between houses \nfor each proportion of owner occupied units built prior to 1940.\n')
else:
    #Fail to reject the null hypothesis 
    print(f'Test Statistic: {f_stat:.2f}')
    print(f'P-value_anova: {p_value_anova:.2f}')
    print('There is not enough evidence to conclude a significant difference in median house values.')