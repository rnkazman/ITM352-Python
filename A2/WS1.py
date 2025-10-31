# Read a file from a URL and write a local file “sales_data_test.csv” file from the first 10 rows of this data.  
import pandas as pd
import pyarrow # not needed, but it's a good practice to import it
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context

# The file at this URL contains a large data set. It must be downloadable and in CSV format to be read by pandas.
url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

# Set display option to show all columns
pd.set_option('display.max_columns', None)

try:
    # Attempt to read the CSV file
    print(f"Reading CSV file...")
    start_time = time.time()

    sales_data = pd.read_csv(url, engine="pyarrow")
    load_time = time.time() - start_time

    print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
    print(f"Number of rows: {len(sales_data)}")
    print(f"Columns: {list(sales_data.columns)}")

    # Ask Pandas to parse the order_date field with a standard representation.
    sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], format='%m/%d/%y', errors='coerce')
    # Replace missing data items with 0.
    sales_data.fillna(0, inplace=True)

    # write 10 rows of sales data as CSV file
    # saving the dataframe
    sales_data.head(10).to_csv('sales_data_test.csv')

except Exception as e:
    print(f"An error occurred: {e}")