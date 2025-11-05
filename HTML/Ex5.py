# Get a JSON file of data. Using a SQL-like query, select data about driver types.
import requests
import pandas as pd
 
# Create a REST query that returns the count of licenses by driver_type
search_results = requests.get("https://data.cityofchicago.org/resource/97wa-y6ff.json?"+
                              "$select=driver_type,count(license)&"+
                              "$group=driver_type")
results_json = search_results.json()

# convert the results to a data frame:
results_df = pd.DataFrame.from_records(results_json)
results_df.columns = ["count", "driver_type"]
results_df = results_df.set_index("driver_type")

# print the results data frame that we created:
print(results_df)