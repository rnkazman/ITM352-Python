def make_basket(customer, items=[]):
    """Create a new basket for a customer, optionally with starting items."""
    return {"customer": customer, "items": items}
 
 
def add_item(basket, name, price, quantity=1):
    """Add an item (name, line cost) to the basket."""
    basket["items"].append((name, price * quantity))
 
 
def basket_total(basket):
    total = 0
    for name, cost in basket["items"]:
        total += cost
    if total > 50:
        total = total * 0.9   # 10% discount on large orders
    return total
 
 
def print_receipt(basket):
    print("Receipt for", basket["customer"])
    for name, cost in basket["items"]:
        print("   ", name.ljust(12), format(cost, "6.2f"))
    print("    TOTAL       ", format(basket_total(basket), "6.2f"))
    print()
 
 
# Alice and Bob start with empty baskets.
alice = make_basket("Alice")
add_item(alice, "apples", 1.25, 4)
add_item(alice, "bread", 3.50)
 
bob = make_basket("Bob")
add_item(bob, "coffee", 11.00)
add_item(bob, "milk", 2.75, 2)
 
# Carol brings a coupon item that starts in her basket.
carol = make_basket("Carol", [("free cookie", 0.00)])
add_item(carol, "cheese", 8.00, 3)
add_item(carol, "crackers", 4.50, 7)
 
print_receipt(alice)
print_receipt(bob)
print_receipt(carol)