# Parse the portions of an email address.
email = input("Enter your UH email address: ")

# Method 1: Using split (Easier)
parts = email.split("@")
username = parts[0]
domain = parts[1]

print(f"Username: {username}")
print(f"Domain: {domain}")

# Method 2: Using index (More manual logic)
at_symbol_index = email.index("@")
username_manual = email[:at_symbol_index]
domain_manual = email[at_symbol_index + 1:]

print(f"Username (manual): {username_manual}")
print(f"Domain (manual): {domain_manual}")