# Determine a movie price.  The rules are:
# If someone is 65 or older, they pay $8.
# If it is Tuesday, the price is $10.
# If it is a matinee, the price is $5 for seniors and $8 otherwise
# Print out the values of the variables and the price.  The price
# should always be the lowest one that applies.

age = 64
day = "Tuesday"
matinee = True
price = 14

if day == "Tuesday":
    price = 10
if age >= 65:
    price =8
if matinee == True:
    if age >= 65:
        price = 5
    else:
        price = 8
        
print("Price is: ", price)