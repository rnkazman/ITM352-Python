# Extracting JSON data from the web example.  This is data on passenger vehicle licenses.

import pandas as pd
from sodapy import Socrata

# The follwowing initializes the Socrata client:
client = Socrata("data.cityofchicago.org", None)

# Modify the following line, using the end of the URL, before the ".json"
results = client.get("rr23-ymwb", limit = 500)

# The following puts the results in a dataframe & prints it:
results_df = pd.DataFrame.from_records(results)
print("Taxi API results:")
print(results_df.head())
