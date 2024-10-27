# Allow users to interactively explore and analyze sales data from a CSV file by providing 
# a simple command-line interface for user interaction.
import pandas as pd
import time
import sys
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Set display.max_rows to None, to force display of all rows
#pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

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
    

def display_rows(data):
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
            
            
def display_menu(data):
    menu_options = (
   ("Show the first n rows of sales data", display_rows),
   ("Show the number of employees by region", employees_by_region),
   ("Exit the program", exit_program)
)

    print("\nAvailable Actions:")
    for index, (description, _) in enumerate(menu_options):
        print(f"{index + 1}. {description}")
    
    try:
        choice = int(input("Select an option (1 to {}): ".format(len(menu_options))))
        if 1 <= choice <= len(menu_options):
            action = menu_options[choice - 1][1]
            action(data)      # Call the selected function
        else:
            print("Invalid choice. Please select a number from the menu.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def exit_program(data):
    sys.exit(0)

# Functions for predefined analytics tasks
def employees_by_region(data):
    pivot_table = pd.pivot_table(data, index='sales_region', values='employee_id', aggfunc=pd.Series.nunique)
    pivot_table.columns = ['Number of Employees']  # Rename the colummn for readability
    print("\nNumber of Employees by Region:")
    print(pivot_table)
    return pivot_table


# Program main loop

#url = 'sales_data_test.csv'
url = "https://drive.google.com/uc?export=download&id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"

# Load the CSV file
sales_data = load_csv(url)

def main():
    # Main loop
    while True:
        display_menu(sales_data)

if __name__ == "__main__":
    main()