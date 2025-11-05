import pandas as pd
import ssl

pd.set_option('display.max_columns', None)

# TEMPORARY FIX: Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K'

try:
    df = pd.read_csv(url, engine="pyarrow")
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

    print(df.head())

except Exception as e:
    print(f"Error reading the file: {e}")
