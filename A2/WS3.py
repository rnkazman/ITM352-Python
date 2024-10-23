
import pandas as pd
import time
import sys

# Set display.max_columns to None, to force display of all columns
pd.set_option("display.max_columns", None)

def load_csv(file_path):
    print(f"Starting to load {file_path}...")
    start_time = time.time()

    try:
        # Attempt to load the CSV file
        df = pd.read_csv(file_path)
        
        # Calculate loading time
        load_time = time.time() - start_time
        
        print(f"File loaded successfully in {load_time:.2f} seconds.")
        print(f"Number of rows: {len(df)}")
        print(f"Columns: {df.columns.to_list()}")

        # List of columns to check
        required_columns = ['quantity', 'unit_price', 'order_date']
        
        # Check for missing columns
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            print(f"\nWarning: The following required columns are missing: {missing_columns}")
        else:
            print("\nAll required columns are present.")

        # We ask Pandas to parse the order_date field to turn it into a standard representation.
        df['order_date'] = pd.to_datetime(df['order_date'], format='mixed')
        
        return df

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
        return None

    except pd.errors.ParserError as e:
        print(f"Error: There was an issue parsing the CSV file:")
        print(str(e))
        return None

    except Exception as e:
        print(f"An unexpected error occurred:")
        print(str(e))
        return None
    

def display_initial_rows(data):
    while True:
        print("\nEnter rows to display:")
        print(f"- Enter a number 1 to {len(data)-1}")
        print("- To see all rows, enter 'all'")
        print("- To skip preview, press Enter")
        user_input = input("Your choice: ").strip().lower()

        if user_input == '':
            print("Skipping data preview.")
            break
        elif user_input == 'all':
            print(data)
            break
        elif user_input.isdigit() and 1 <= int(user_input) < len(data):
            print(data.head(int(user_input)))
            break
        else:
            print("Invalid input. Please use the specified formats.")


url = 'sales_data_test.csv'
#url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

# Load the CSV file
sales_data = load_csv(url)

def main():
    # Main loop
    while True:
        display_initial_rows(sales_data)

if __name__ == "__main__":
    main()