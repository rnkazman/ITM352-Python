# Read in a CSV file and turn it into a Pandas dataframe
import numpy as np
import pandas as pd

df_homes = pd.read_csv("homes_data.csv")

# Print out the dimensions of the data frame and show the first 10 rows
shape = df_homes.shape
print(f"The homes data has {shape[0]} rows and {shape[1]} columns")

# Select only properties that have 500 or more units 
df_big_apartments = df_homes[df_homes.units >= 500]

# Drop some unnecessary columns and print the first 10 rows
df_big_apartments = df_big_apartments.drop(columns=['id','easement'])
print("First 10 rows:\n",df_homes.head(10))

# Look at the data types
print(df_big_apartments.info())

# Since some of the data types are incorrect, coerce them to the correct data type 
df_big_apartments['land_sqft'] = pd.to_numeric(df_big_apartments['land_sqft'], errors='coerce')
df_big_apartments['gross_sqft'] = pd.to_numeric(df_big_apartments['gross_sqft'], errors='coerce')
df_big_apartments['sale_price'] = pd.to_numeric(df_big_apartments['sale_price'], errors='coerce')

# Look at the data types now and print the cleaned data
print(df_big_apartments.info())
print("After cleaning:\n", df_big_apartments.head(10))

# We have some null values.  Let's drop those rows.
df_big_apartments = df_big_apartments.dropna()

# Now drop duplicate records
df_big_apartments = df_big_apartments.drop_duplicates(df_big_apartments.columns, keep='first')

print("After dropping nulls and duplicates:\n", df_big_apartments.head(10))

df_big_apartments = df_big_apartments[df_big_apartments['sale_price']> 0]

print("After filtering out 0 sales:\n", df_big_apartments.head(10))
print("The average sales price of big apartments is: $", round(df_big_apartments['sale_price'].mean(),2))