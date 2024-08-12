# Read in a CSV file with sales data 
# Create a pivot table that shows sales by order and customer type, summing the
# quantity and sales price per row.

import pandas as pd
pd.set_option("display.float_format", "${:,.2f}".format)

sales_data = pd.read_csv(
 "sales_data.csv",
 parse_dates=["order_date"],
 dayfirst=True, ).convert_dtypes(dtype_backend="pyarrow")


pivot = sales_data.pivot_table(
   values=["sale_price", "quantity"], 
   index=["order_type", "customer_type"],
   aggfunc="sum", fill_value=0,
).loc[:,["sale_price","quantity"]]

pd.set_option("display.max_columns", None)

print(pivot)