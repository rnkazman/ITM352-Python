# Extracting JSON data from the web example.  This is data on passenger vehicle licenses.
import pandas as pd
from sodapy import Socrata

# Initialize the Socrata client
client = Socrata("data.cityofchicago.org", None)

# Specify the JSON file we want to get from the client 
results = client.get("rr23-ymwb", limit = 500)

# Print the results as stored in the DataFrame 
results_df = pd.DataFrame.from_records(results)
print("Taxi API results:")
print(results_df.head())

vehicles_and_fuel_sources = results_df[["public_vehicle_number", "vehicle_fuel_source"]]
print(f"Vehicles and fuel sources: \n{vehicles_and_fuel_sources}")

vehicles_by_fuel_type = vehicles_and_fuel_sources.groupby("vehicle_fuel_source")
print(vehicles_by_fuel_type.count())