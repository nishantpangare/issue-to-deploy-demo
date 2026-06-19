def calculate_discount(price, discount_percent):
    # BUG: price comes in as string, no type conversion
    return price - (price * discount_percent / 100)

def get_user(user_id):
    users = {
        1: {"name": "Alice", "email": "alice@example.com"},
        2: {"name": "Bob", "email": "bob@example.com"}
    }
    # BUG: no handling if user_id not found
    return users[user_id]
