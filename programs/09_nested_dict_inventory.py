"""
Program 9: Nest dictionaries – inventory of products with price and stock
Concept: Dictionaries (nesting, access, update)
"""

def inventory_management():
    """Demonstrate nested dictionaries for product inventory management."""
    
    # Create nested dictionary for inventory
    inventory = {
        "Laptop": {
            "price": 999.99,
            "stock": 15,
            "category": "Electronics"
        },
        "Mouse": {
            "price": 29.99,
            "stock": 50,
            "category": "Electronics"
        },
        "Keyboard": {
            "price": 79.99,
            "stock": 30,
            "category": "Electronics"
        },
        "Notebook": {
            "price": 4.99,
            "stock": 100,
            "category": "Stationery"
        },
        "Pen": {
            "price": 1.99,
            "stock": 200,
            "category": "Stationery"
        }
    }
    
    print("Initial Inventory:")
    print("=" * 50)
    for product, details in inventory.items():
        print(f"{product}:")
        print(f"  Price: ${details['price']:.2f}")
        print(f"  Stock: {details['stock']} units")
        print(f"  Category: {details['category']}")
        print()
    
    # Access specific product information
    print("Accessing specific product information:")
    product_name = "Laptop"
    if product_name in inventory:
        product_info = inventory[product_name]
        print(f"{product_name} - Price: ${product_info['price']:.2f}, Stock: {product_info['stock']}")
    print()
    
    # Update stock after a sale
    print("Updating stock after selling 3 Laptops:")
    if "Laptop" in inventory:
        inventory["Laptop"]["stock"] -= 3
        print(f"Laptop stock updated: {inventory['Laptop']['stock']} units remaining")
    print()
    
    # Update price due to sale
    print("Updating price for Mouse (10% off):")
    if "Mouse" in inventory:
        original_price = inventory["Mouse"]["price"]
        discount = 0.10
        inventory["Mouse"]["price"] *= (1 - discount)
        print(f"Mouse price: ${original_price:.2f} -> ${inventory['Mouse']['price']:.2f}")
    print()
    
    # Add new product
    print("Adding new product: Monitor")
    inventory["Monitor"] = {
        "price": 299.99,
        "stock": 25,
        "category": "Electronics"
    }
    print(f"Added Monitor: ${inventory['Monitor']['price']:.2f}, Stock: {inventory['Monitor']['stock']}")
    print()
    
    # Remove discontinued product
    print("Removing discontinued product: Pen")
    if "Pen" in inventory:
        del inventory["Pen"]
        print("Pen removed from inventory")
    print()
    
    # Display final inventory
    print("Final Inventory:")
    print("=" * 50)
    total_value = 0
    for product, details in inventory.items():
        product_value = details['price'] * details['stock']
        total_value += product_value
        print(f"{product}:")
        print(f"  Price: ${details['price']:.2f}")
        print(f"  Stock: {details['stock']} units")
        print(f"  Category: {details['category']}")
        print(f"  Value: ${product_value:.2f}")
        print()
    
    print(f"Total Inventory Value: ${total_value:.2f}")

if __name__ == "__main__":
    inventory_management()