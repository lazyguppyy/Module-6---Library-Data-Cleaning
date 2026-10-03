#MODULE 6: Library Data Cleaning
#author: Logan Grisby
#assignment: Option #1 - choose a dataset and clean the data by removing missing or erroneous values and filling gaps with appropriate values, and perform an exploratory data analysis (EDA).

import pandas as pd

#This function is used to retrieve data from CSV files in the form of a data frame.
df = pd.read_csv("library_usage.csv")

#Returns the top 5 values of a data frame.
print("First five rows:")
print(df.head())
print("\n")

#Returns the data frame of boolean values.
##Missing values are mapped to True and non-missing value gets mapped to False.
print("\nMissing values:")
print(df.isnull().sum())
print("\n")

#Drops rows and/or columns with Null values.
df = df.dropna()

#Removes erroneous values.
df = df[df["Visits"] >= 0]

#Cleaned data frame
print("Cleaned data:")
print(df)
print("\n")

#Generates summary statistic
print("Summary statistics:")
print(df.describe())