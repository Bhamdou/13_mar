def add_product(inventory, name, price, quantity):
    product = {'name': name, 'price': price, 'quantity': quantity}
    inventory.append(product)
    return inventory

def remove_product(inventory, name):
    product_index = -1
    for i, product in enumerate(inventory):
        if product['name'] == name:
            product_index = i
            break
    if product_index == -1:
        print(f"Product {name} not found in inventory.")
    else:
        del inventory[product_index]
    return inventory

def update_price(inventory, name, price):
    product_index = -1
    for i, product in enumerate(inventory):
        if product['name'] == name:
            product_index = i
            break
    if product_index == -1:
        print(f"Product {name} not found in inventory.")
    else:
        inventory[product_index]['price'] = price
    return inventory

def update_quantity(inventory, name, quantity):
    product_index = -1
    for i, product in enumerate(inventory):
        if product['name'] == name:
            product_index = i
            break
    if product_index == -1:
        print(f"Product {name} not found in inventory.")
    else:
        inventory[product_index]['quantity'] = quantity
    return inventory

def display_inventory(inventory):
    print("Inventory:")
    total_value = 0
    for product in inventory:
        value = product['price'] * product['quantity']
        total_value += value
        print(f"Product: {product['name']}, Price: ${product['price']}, Quantity: {product['quantity']}, Value: ${value}")
    print(f"\nTotal value of all products in stock: ${total_value}")

inventory = []
inventory = add_product(inventory, 'Product A', 10.0, 5)
inventory = add_product(inventory, 'Product B', 20.0, 3)
inventory = add_product(inventory, 'Product C', 30.0, 2)
inventory = remove_product(inventory, 'Product D')
inventory = update_price(inventory, 'Product A', 15.0)
inventory = update_quantity(inventory, 'Product B', 4)
display_inventory(inventory)
