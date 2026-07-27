# the shopping cart bug
def add_to_cart(item, cart=None):# cart=None means every function call starts with cart as None

    if cart is None: # if cart is none then cretes a new empty list 
        cart =[]
    cart.append(item) # and then only add the items
    return cart

print(add_to_cart("pen"))
print(add_to_cart("book"))
print(add_to_cart("bag"))