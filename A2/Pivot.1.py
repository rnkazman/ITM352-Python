# Read in a CSV file with sales data and print the first 5 rows.
# Need to install Pandas and pyarrow for this to work.
import pandas as pd

# We choose dtype_backend="pyarrow" as this is more memory efficient than dtype_backend="numpy"
sales_data = pd.read_csv(
 "sales_data.csv").convert_dtypes(dtype_backend="pyarrow")

# We ask Pandas to parse the order_date field to turn it into a standard representation.
sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], format='mixed')

# Set display.max_columns to None, to force display of all columns
pd.set_option("display.max_columns", None)

print(sales_data.head(5))