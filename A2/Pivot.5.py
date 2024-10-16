# Read in a CSV file with sales data 
# Create a pivot table with sub-rows showing sales by customer type and order type.
# Show this by state.

import pandas as pd
pd.set_option("display.float_format", "${:,.2f}".format)

# We choose dtype_backend="pyarrow" as this is more memory efficient than dtype_backend="numpy"
sales_data = pd.read_csv(
 "sales_data.csv").convert_dtypes(dtype_backend="pyarrow")

# We ask Pandas to parse the order_date field to turn it into a standard representation.
sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], format='mixed')


pivot = sales_data.pivot_table(
   values="sale_price", index=["customer_type", "order_type", "customer_state"],
   columns="product_category",
   aggfunc="sum", fill_value=0,
)

pd.set_option("display.max_columns", None)

print(pivot)