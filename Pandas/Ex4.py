# Read a json file of taxi trip data and create a dataframe from it.
import pandas as pd

results_df = pd.read_json("Taxi_Trips.json")

# Print summary statistics about the dataframe, as well as the median.
print(results_df.describe())
print(results_df.head())
print("The median fare value is: ", results_df['fare'].median())
