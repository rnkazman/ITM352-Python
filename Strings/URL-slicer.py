url = input("Enter a URL: ")

# 1. Strip off the protocol
clean_url = url.replace("https://", "")

# 2. Split by the dots
parts = clean_url.split(".")

# 3. Grab the domain and the TLD 
domain = parts[1]
TLD = parts[2]

print(f"The domain is: {domain}")
print(f"The TLD is: {TLD}")