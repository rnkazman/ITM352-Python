# Read in a CSV file with sales data 
# Create a pivot table with sub-rows showing sales by customer type and order type.
# Show this by state.

import pandas as pd
pd.set_option("display.float_format", "${:,.2f}".format)

sales_data = pd.read_csv(
 "sales_data.csv",
 parse_dates=["order_date"],
 dayfirst=True, ).convert_dtypes(dtype_backend="pyarrow")


pivot = sales_data.pivot_table(
   values="sale_price", index=["customer_type", "order_type", "customer_state"],
   columns="product_category",
   aggfunc="sum", fill_value=0,
)

pd.set_option("display.max_columns", None)

print(pivot)