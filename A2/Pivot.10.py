# Read in a CSV file with sales data 
# Create a pivot table that shows the number of employees by region.
# Need to create a function to only count unique employees.

# Function that takes, as input, a Pandas series, and returns the number of unique elements in that series
def count_unique(values):
    return len(values.unique())


import pandas as pd
pd.set_option("display.float_format", "${:,.2f}".format)

# We choose dtype_backend="pyarrow" as this is more memory efficient than dtype_backend="numpy"
sales_data = pd.read_csv(
 "sales_data.csv").convert_dtypes(dtype_backend="pyarrow")

# Ask Pandas to parse the order_date field to turn it into a standard representation.
sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], format='mixed')

# Calculate the number of unique employees per region
pivot = sales_data.pivot_table(
   values=["employee_id"], 
   index="sales_region", 
   aggfunc=count_unique 
)

pd.set_option("display.max_columns", None)

print(pivot)