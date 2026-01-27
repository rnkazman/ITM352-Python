# this program shows how scope works in Python


def calculate_discounted_price(price):
    global discount 
    discount = 0.6  
    discounted_price = price * discount
    print(f"Inside function, discounted price: {discounted_price:.2f}")
    discount = 0.8  
    return discounted_price

# Global scope
price = 100.0

print(f"Original price in main program: {price:.2f}")

discount = 0.9  # global scope
discounted = calculate_discounted_price(price)
print(f"Discounted price returned to main program: {discounted:.2f}")
print("Discount = ", discount)  # This will raise an error since discount is not defined in global scope