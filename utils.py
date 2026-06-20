def calculate_discount(price, discount_percent):
    # Convert price to float to ensure arithmetic operations work correctly
    numeric_price = float(price)
    return numeric_price - (numeric_price * discount_percent / 100)

def get_user(user_id):
    users = {
        1: {"name": "Alice", "email": "alice@example.com"},
        2: {"name": "Bob", "email": "bob@example.com"}
    }
    # BUG: no handling if user_id not found
    return users[user_id]