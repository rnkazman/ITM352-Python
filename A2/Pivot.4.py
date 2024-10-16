# Read in a CSV file with sales data 
# Create a pivot table, aggregating sales by region.
# Change the sub-columns to showing the quantity by state, by sale type (retail or wholesale), and also 
#  show the max quantity per state.  Also, replaced N/A values with 0.

import pandas as pd
pd.set_option("display.float_format", "${:,.2f}".format)

# We choose dtype_backend="pyarrow" as this is more memory efficient than dtype_backend="numpy"
sales_data = pd.read_csv(
 "sales_data.csv").convert_dtypes(dtype_backend="pyarrow")

# We ask Pandas to parse the order_date field to turn it into a standard representation.
sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], format='mixed')

pivot = sales_data.pivot_table(
   values="quantity", index="customer_state", columns=["customer_type", "order_type"],
   aggfunc="max", margins=True, margins_name="Max Quantity", fill_value=0,
)

pd.set_option("display.max_columns", None)

print(pivot)