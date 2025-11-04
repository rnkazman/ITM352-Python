import mysql.connector
from flask import Flask, render_template, request
import locale

# Set the locale to the desired currency format (e.g., U.S. Dollars)
# On Linux/macOS, use 'en_US.UTF-8'. On Windows, 'English_United States' or 'en_US'.
try:
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') 
except locale.Error:
    # Fallback for systems that don't recognize the UTF-8 suffix
    locale.setlocale(locale.LC_ALL, 'en_US')

# --- Configuration ---
# REPLACE THESE WITH YOUR ACTUAL MySQL CREDENTIALS
DB_CONFIG = {
    'user': 'root',        # e.g., 'root'
    'password': '',    # e.g., 'mypassword'
    'host': '127.0.0.1',        # Usually 'localhost' or '127.0.0.1'
    'port': 3307,               # The port you specified
    'database': 'TestTravel'
}
# ---------------------

app = Flask(__name__)

def get_db_connection():
    """Establishes a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    """Handles the main page, form submission, and displays results."""
    rooms = None
    min_price = 0
    max_price = 0
    error_message = None

    if request.method == 'POST':
        try:
            # 1. Get form data and validate
            min_price = float(request.form.get('min_price', 0))
            max_price = float(request.form.get('max_price', 99999))
            
            if min_price < 0 or max_price < 0:
                 raise ValueError("Prices cannot be negative.")
            if min_price > max_price:
                 # Swap if min is greater than max for a valid range
                 min_price, max_price = max_price, min_price
                 
            # 2. Connect to the database
            conn = get_db_connection()
            if conn is None:
                error_message = "Could not connect to the database. Check credentials/server status."
            else:
                cursor = conn.cursor(dictionary=True)
                # 3. Construct and execute the SQL query
                query = """
                SELECT R.roomNo, R.hotelNo, R.type, R.price, H.hotelName, H.city
                FROM Room R
                JOIN Hotel H ON R.hotelNo = H.hotelNo
                WHERE R.price BETWEEN %s AND %s
                ORDER BY R.price;
                """
                cursor.execute(query, (min_price, max_price))
                rooms = cursor.fetchall()
                
                # 4. Close connections
                cursor.close()
                conn.close()

        except ValueError as e:
            error_message = f"Invalid input: Please enter valid numbers for the price range. {e}"
        except Exception as e:
            error_message = f"An unexpected error occurred: {e}"

    # Render the template with the data
    #print(min_price, max_price)
    #print(type(min_price), type(max_price))
    min_price_str = locale.currency(min_price, grouping=True)
    max_price_str = locale.currency(max_price, grouping=True)

    return render_template('index.html', 
                           rooms=rooms, 
                           min_price=min_price_str, 
                           max_price=max_price_str,
                           error=error_message)


if __name__ == '__main__':
    # Flask will run on http://127.0.0.1:5000/ by default
    app.run(debug=True)
