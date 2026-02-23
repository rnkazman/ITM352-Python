# Get a name from the user and put it in title case
raw_name = input("Enter your name:")

# Strip whitespace and capitalize the first letter of each word
clean_name = raw_name.strip().title()

print(f"Cleaned name: '{clean_name}'")