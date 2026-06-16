### EFFECTIVE DATA ANALYSIS BY APPLYING DESCRIPTIVE STATISTICS

###### Context:
    
""" The Boston Housing Dataset is a derived from information collected by the U.S. Census Service 
concerning housing in the area of Boston MA. The following describes the dataset columns:

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

## Import Libraries

import pandas as pd
import numpy as np
import seaborn as sns

# import os for 
import os 
os.makedirs("output", exist_ok=True)

# Store all the output plots in a PDF , instead of plt.show - store in PDF file
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
with PdfPages("output/descriptive_statistics_analysis_report.pdf") as pdf:
    
### 1: Load Dataset from Boston Housing Agency into a DataFrame.
# Load Dataset from Boston Housing Agency.csv
    df = pd.read_csv("boston_housing_descriptive_analysis.csv")
    print(df.head())

### 2: For the "Median value of owner-occupied homes" provide a boxplot. 
# BOXPLOT - "Median value of owner-occupied homes" 

    plt.figure(figsize=(6, 4))
# Adjust outlier appearance
    sns.boxplot(x='MEDV', data=df, color='lightgreen', linewidth=2, flierprops=dict(marker='o', markersize=6
                                                                                , markerfacecolor='red', linestyle=''
                                                                                , label='Out Layer')) 
plt.title('\nBoxplot: Median Value of Owner-Occupied Homes\n', fontsize =14)
plt.xlabel('Median Value ($1000)', fontsize =12)

# Add median line
plt.axvline(df['MEDV'].median(), color='red', linestyle='--', label='Median Value')  
plt.legend(fontsize=10)
plt.tight_layout()
pdf.savefig(bbox_inches="tight")
#plt.show()

#plt.savefig("output/median_value_of_owner_occupied_homes.png", dpi=300, bbox_inches="tight") 
# plt.close()
#plt.show()

# 2 continue: REMOVING THE OUTLIERS
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

plt.title('\nWithout outliers : Median Value of Owner-Occupied Homes (in $1000)\n', fontsize =14)
plt.xlabel('Median Value ($1000)')
# Add median line
plt.axvline(df_no_outliers['MEDV'].median(), color='red', linestyle='--', label='Median Value')  
plt.legend(fontsize=10)
plt.tight_layout()
pdf.savefig(bbox_inches="tight")
#plt.show()


### 3: Provide a histogram for the “Charles river variable”. 

# histogram for the “Charles river variable

plt.figure(figsize=(6, 4))
sns.histplot(df['CHAS'], bins=2, color ='brown') 
plt.title('\nHistogram of Charles River Variable (CHAS)\n')
plt.xlabel('Charles River Variable')

# Add gridlines
plt.grid(True)  
plt.tight_layout()
pdf.savefig()
#plt.show()

### 4: Provide a boxplot for the MEDV variable vs the AGE variable. 
# (Discretize the age variable into three groups of 35% or less, between 35 and 70% and 70% and over) 

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
plt.tight_layout()
pdf.savefig(bbox_inches="tight")
#plt.show()

### 5: Provide a scatter plot to show the relationship between Nitric oxide concentrations (NOX) 
# and the proportion of non-retail business acres per town (INDUS).
# What can you say about the relationship?

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
plt.tight_layout()
pdf.savefig(bbox_inches="tight")
#plt.show()


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


### 6: Create a histogram for the pupil to teacher ratio variable (PTRATIO)

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
pdf.savefig(bbox_inches="tight")

    ### 7: Is there a significant difference in median value of houses bounded by the Charles river
    # or not? (CHAS) (T-test for independent samples)

from scipy.stats import ttest_ind

# Subset the data based on charless river value(0 or 1)
river_houses = df[df['CHAS'] == 1]['MEDV']
nonriver_houses = df[df['CHAS'] == 0]['MEDV']

# Perform t-test  ## p-->probability
t_stat, p_value = ttest_ind(river_houses, nonriver_houses)

# Define significance level - consider as alpha
sig_level_alpha = 0.05

# Create a text figure for t-test results
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('off')

result_text = f"T-TEST: Charles River Impact on House Values\n\n"
result_text += f"Test Statistic: {t_stat:.4f}\n"
result_text += f"P-value: {p_value:.6f}\n"
result_text += f"Significance Level (α): {sig_level_alpha}\n\n"

if p_value < sig_level_alpha:
    result_text += "Result: REJECT NULL HYPOTHESIS\n\n"
    result_text += "Conclusion:\n"
    result_text += "There is a significant difference in median house values\n"
    result_text += "between houses bounded by the Charles River and those\n"
    result_text += "not bounded by the river."
else:
    result_text += "Result: FAIL TO REJECT NULL HYPOTHESIS\n\n"
    result_text += "Conclusion:\n"
    result_text += "There is not enough evidence to conclude a significant\n"
    result_text += "difference in median house values."

ax.text(0.1, 0.5, result_text, fontsize=11, verticalalignment='center',
        family='monospace', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
plt.tight_layout()
pdf.savefig(bbox_inches="tight")
plt.close()

### 8: Is there a difference in Median values of houses (MEDV) for each proportion of owner occupied
#  units built prior to 1940 (AGE)? (ANOVA)

from scipy.stats import f_oneway

age_groups = [df[df['AGE_group'] == group]['MEDV'] for group in df['AGE_group'].unique()]

# Perform ANOVA
f_stat, p_value_anova = f_oneway(*age_groups)

# Define significance level - consider as alpha
sig_level_alpha = 0.05

# Create a text figure for ANOVA results
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('off')

result_text = f"ANOVA: House Values Across AGE Groups\n\n"
result_text += f"Test Statistic (F): {f_stat:.4f}\n"
result_text += f"P-value: {p_value_anova:.6f}\n"
result_text += f"Significance Level (α): {sig_level_alpha}\n\n"

if p_value_anova < sig_level_alpha:
    result_text += "Result: REJECT NULL HYPOTHESIS\n\n"
    result_text += "Conclusion:\n"
    result_text += "There is a significant difference in median house values\n"
    result_text += "for each proportion of owner-occupied units built\n"
    result_text += "prior to 1940 (AGE groups)."
else:
    result_text += "Result: FAIL TO REJECT NULL HYPOTHESIS\n\n"
    result_text += "Conclusion:\n"
    result_text += "There is not enough evidence to conclude a significant\n"
    result_text += "difference in median house values across AGE groups."

ax.text(0.1, 0.5, result_text, fontsize=11, verticalalignment='center',
        family='monospace', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
plt.tight_layout()
pdf.savefig(bbox_inches="tight")
plt.close()

pdf.close()
#plt.show()
