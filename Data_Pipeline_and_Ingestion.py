#Context: Explore US Bikeshare Data

#Analyze the Bicycle-sharing data for three major cities in the United States—Chicago, New York City, and Washington.
#The datasets used for this project contain bike share data for the first six months of 2017. The csv files can be found in the same folder. 
#The data is provided by Motivate, which is a bike share system provider for many cities in the United States.  

#Load the new_york_city csv file 
import pandas as pd
df_newyork_city = pd.read_csv("newyork_city_data_pipeline_small.csv")
print("New York City Data:", df_newyork_city.head())

#Load the washington csv file 
df_washington = pd.read_csv("washington_data_pipeline_small.csv")
print("Washington Data:", df_washington.head())

#Load the chicago csv file 
df_chicago = pd.read_csv("chicago_data_pipeline_small.csv")
print("Chicago Data:", df_chicago.head())

# Concatenate all dataframes into a single dataframe --> So that can compare and analyse all the data.
df_all_data = pd.concat([df_newyork_city, df_washington, df_chicago])

# Convert 'Start Time' dates column to datetime objects using pd.to_datetime
df_all_data['Start Time'] = pd.to_datetime(df_all_data['Start Time'])

df_all_data.head()

# 1. most popular month for start time?

import calendar
# Extract the month from 'Start Time'
df_all_data['Month'] = df_all_data['Start Time'].dt.month

# Most popular month 
most_popular_month = df_all_data['Month'].value_counts().idxmax()

print("\nMost popular month for start time: ", most_popular_month, "th Month" "\n")
print("Month Name: ",calendar.month_name[most_popular_month], "\n")

# 2. Most popular day of week (Monday, Tuesday, etc.) for start time?

# Extract day of week from datetime
df_all_data['Day_of_week'] = df_all_data['Start Time'].dt.day_name()

# Most popular day of week
most_popular_day = df_all_data['Day_of_week'].value_counts().idxmax()
print("\nMost popular day of week for start time:", most_popular_day,"\n")

#3. # most popular hour of day for start time?
# Extract hour from datetime
df_all_data['Hour'] = df_all_data['Start Time'].dt.hour

# Most popular hour of day
most_popular_hour = df_all_data['Hour'].value_counts().idxmax()

print("\nMost popular hour of day for start time:", most_popular_hour,"\n")

#4. total trip duration and average trip duration?

# Total trip duration and average trip duration - trip duration column value is in seconds
total_trip_duration = df_all_data['Trip Duration'].sum()
average_trip_duration = df_all_data['Trip Duration'].mean()

print("\nTotal trip duration:", total_trip_duration, "seconds")
print("Average trip duration:", average_trip_duration, "seconds")

# Convert total trip duration from seconds to hours, minutes, and seconds in more meaningful formats to read. 1 Hour = 3600 seconds
hours, remainder = divmod(total_trip_duration, 3600)
minutes, seconds = divmod(remainder, 60)
print("\nTotal trip duration in Hours, Minutes and Seconds in more meaningful format: ", "\nhours   : ", round(hours), "\nminutes : ",round(minutes) , "\nseconds : ",round(seconds))

# Convert total trip duration from seconds to hours, minutes, and seconds in more meaningful formats to read
avg_hours, avg_remainder = divmod(average_trip_duration, 3600)
avg_minutes, avg_seconds = divmod(avg_remainder, 60)
print("\nAverage trip duration in Hours, Minutes and Seconds in more meaningful format: ", "\nhours   : ", round(avg_hours), "\nminutes : ",round(avg_minutes) , "\nseconds : ",round(avg_seconds),"\n")

#5. most popular start station and most popular end station?

# Most popular start station and end station
most_popular_start_station = df_all_data['Start Station'].value_counts().idxmax()
most_popular_end_station = df_all_data['End Station'].value_counts().idxmax()

print("\nMost popular start station:", most_popular_start_station)
print("Most popular end station:", most_popular_end_station,"\n")

#6 . most popular trip?

# Most popular trip
#most_popular_trip = df_all_data.groupby(['Start Station', 'End Station']).size().idxmax()
most_popular_trip = df_all_data.groupby(['Start Station', 'End Station']).size()
print("\nMost popular trip:", most_popular_trip.idxmax(),"\n")
print("Most popular trip - counts:", most_popular_trip.max(),"\n")

#7. Counts of each user type?

# Counts of each user type
user_type_counts = df_all_data['User Type'].value_counts()

print("\nCounts of each user type:")
print(user_type_counts,"\n")