def calculate_discount(price, discount_percent):
    # Fix: Convert price to a float to avoid type errors
    price_float = float(price)
    return price_float - (price_float * discount_percent / 100)

def get_user(user_id):
    users = {
        1: {"name": "Alice", "email": "alice@example.com"},
        2: {"name": "Bob", "email": "bob@example.com"}
    }
    # Fix: Use .get() to safely retrieve user; returns None if user_id not found
    return users.get(user_id)