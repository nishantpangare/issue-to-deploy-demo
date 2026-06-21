def calculate_discount(price, discount_percent):
    # BUG: price comes in as string, no type conversion
    price_numeric = float(price)
    return price_numeric - (price_numeric * discount_percent / 100)

def get_user(user_id):
    users = {
        1: {"name": "Alice", "email": "alice@example.com"},
        2: {"name": "Bob", "email": "bob@example.com"}
    }
    # BUG: no handling if user_id not found
    return users[user_id]