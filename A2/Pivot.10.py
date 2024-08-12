# Read in a CSV file with sales data 
# Create a pivot table that shows the number of employees by region.
# Need to create a function to only count unique employees.

# Function that takes, as input, a Pandas series, and returns the number of unique elements in that series
def count_unique(values):
    return len(values.unique())


import pandas as pd
pd.set_option("display.float_format", "${:,.2f}".format)

sales_data = pd.read_csv(
 "sales_data.csv",
 parse_dates=["order_date"],
 dayfirst=True, ).convert_dtypes(dtype_backend="pyarrow")

# Calculate the number of unique employees per region
pivot = sales_data.pivot_table(
   values=["employee_id"], 
   index="sales_region", 
   aggfunc=count_unique 
)

pd.set_option("display.max_columns", None)

print(pivot)