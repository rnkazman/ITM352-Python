# Read in a CSV file with sales data 
# Create a pivot table, aggregating sales by region, with columns defined by order_type (which is either Retail or Wholesale).
# Add in sub-columns showing the average sales by state, by sale type (retail or wholesale).

import pandas as pd
pd.set_option("display.float_format", "${:,.2f}".format)

# We choose dtype_backend="pyarrow" as this is more memory efficient than dtype_backend="numpy"
sales_data = pd.read_csv(
 "sales_data.csv").convert_dtypes(dtype_backend="pyarrow")

# We ask Pandas to parse the order_date field to turn it into a standard representation.
sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], format='mixed')

pivot = sales_data.pivot_table(
   values="sale_price", index="customer_state", columns=["customer_type", "order_type"],
   aggfunc="mean", 
)

pd.set_option("display.max_columns", None)

print(pivot)